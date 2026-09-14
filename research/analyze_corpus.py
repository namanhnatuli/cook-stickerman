#!/usr/bin/env python3
"""
Reproducible Corpus Analysis Script for cook-stickerman benchmark transcripts.

NOTE ON TOKENIZER SCOPE & LIMITATIONS:
This script implements an engineering heuristic for sentence tokenization and word counting,
optimized for measuring pacing cadence, word counts, and sentence length distributions in
spoken culinary explainer transcripts. It is NOT an exhaustive NLP linguistic segmentation model.

Methodology & Rules:
1. Strips non-spoken audio tags via an explicit allowlist (e.g., '[music]', '[background-music]',
   '[snorts]', '[applause]', '[laughter]', '[inaudible]', '[noise]') while preserving semantic
   bracketed tags (e.g., '[Chapter 1]').
2. Protects decimals in numbers (e.g., '120.5 C', '2.3 million') so numbers do not split sentences.
3. Protects honorifics, titles, and non-terminal abbreviations (e.g., 'vs.', 'etc.', 'Mr.', 'Dr.').
4. Protects internal dots of multi-dot abbreviations (e.g., 'B.C.E.', 'C.E.', 'U.S.', 'U.S.A.',
   'e.g.', 'i.e.'). Evaluates trailing dots contextually: treats as a sentence boundary if followed
   by sentence-starter words, but protects the dot if acting as a modifier/adjective before nouns
   (e.g., 'The U.S. Market expanded') or within explanatory clauses.
5. Splits sentences on standard terminal punctuation: '.', '!', '?'.
6. Filters out empty sentence segments and restores protected characters.
7. Computes tokenized word count, sentence count, mean, median, and sentences exceeding 28 words.
8. Shared aggregation logic (`aggregate_results`) used by both `main()` and the `unittest` suite.
"""

import glob
import os
import re
import statistics
import sys
import unittest

AUDIO_TAG_PATTERN = re.compile(
    r'\[(?:music|background[- ]music|snorts?|applause|laughter|inaudible|noise)\]',
    re.IGNORECASE
)

SENTENCE_STARTER_WORDS = (
    r'Then|It|He|She|They|We|You|This|That|These|Those|There|Here|'
    r'However|Moreover|Furthermore|Therefore|After|Before|Later|Meanwhile|'
    r'Once|When|While|Now|Next|So|And|But|If|Because|Although|Since|What|Why|How'
)

def clean_and_tokenize(raw_text):
    if not raw_text or not raw_text.strip():
        return []

    # Step 1: Strip allowed non-spoken audio cue tags only
    cleaned = AUDIO_TAG_PATTERN.sub('', raw_text)

    # Step 2: Protect decimals in numbers (e.g., '120.5 C', '2.3 million')
    cleaned = re.sub(r'(\d+)\.(\d+)', r'\1<DOT>\2', cleaned)

    # Step 3: Protect honorifics/titles (Mr., Dr., etc.) where dot is never a sentence-terminal delimiter
    cleaned = re.sub(r'\b(mr|mrs|ms|dr|prof|sr|jr|vs|vol|no)\.', r'\1<ABBR_DOT>', cleaned, flags=re.IGNORECASE)

    # Step 4: Multi-dot abbreviations (B.C.E., C.E., U.S.A., U.S., e.g., i.e.)
    def protect_internal_dots(m):
        parts = m.group(0).split('.')
        return '<ABBR_DOT>'.join(parts[:-1]) + '.'

    cleaned = re.sub(r'\b(B\.C\.E\.|C\.E\.|U\.S\.A\.|U\.S\.|e\.g\.|i\.e\.)', protect_internal_dots, cleaned, flags=re.IGNORECASE)

    # Protect trailing dot if followed by comma, semicolon, colon, or lowercase word
    cleaned = re.sub(r'([A-Za-z]<ABBR_DOT>[A-Za-z0-9<ABBR_DOT>]*)\.(?=[,\s;:]+[a-z])', r'\1<ABBR_DOT>', cleaned)
    cleaned = re.sub(r'([A-Za-z]<ABBR_DOT>[A-Za-z0-9<ABBR_DOT>]*)\.(?=[,;:])', r'\1<ABBR_DOT>', cleaned)

    # Contextual check for U.S. / U.S.A.: protect trailing dot when followed by a noun (e.g., 'U.S. Market')
    cleaned = re.sub(
        r'\b(U<ABBR_DOT>S|U<ABBR_DOT>S<ABBR_DOT>A)\.(?=\s+(?!' + SENTENCE_STARTER_WORDS + r'\b)[A-Z][a-z]+)',
        r'\1<ABBR_DOT>',
        cleaned
    )

    # Contextual check for e.g. / i.e.: protect trailing dot unless followed by a sentence starter
    cleaned = re.sub(
        r'\b(e<ABBR_DOT>g|i<ABBR_DOT>e)\.(?=\s+(?!' + SENTENCE_STARTER_WORDS + r'\b)[A-Za-z]+)',
        r'\1<ABBR_DOT>',
        cleaned,
        flags=re.IGNORECASE
    )

    # Step 5: Split sentences on terminal punctuation (. ! ?)
    raw_sentences = re.split(r'[.!?]+', cleaned)

    # Step 6: Clean and tokenize sentences
    sentences = []
    for s in raw_sentences:
        s_restored = s.replace('<DOT>', '.').replace('<ABBR_DOT>', '.')
        words = s_restored.strip().split()
        if words:
            sentences.append(words)
    return sentences

def analyze_text(raw_text, filename='<memory>'):
    sentences = clean_and_tokenize(raw_text)
    total_words = sum(len(w) for w in sentences)
    sentence_count = len(sentences)
    sentence_lengths = [len(w) for w in sentences]

    mean_len = (total_words / sentence_count) if sentence_count > 0 else 0.0
    median_len = statistics.median(sentence_lengths) if sentence_lengths else 0.0
    gt_28 = sum(1 for l in sentence_lengths if l > 28)

    return {
        'filename': filename,
        'words': total_words,
        'sentences': sentence_count,
        'lengths': sentence_lengths,
        'mean': mean_len,
        'median': median_len,
        'gt_28': gt_28
    }

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    return analyze_text(raw_text, filename=os.path.basename(filepath))

def aggregate_results(results):
    """
    Centralized aggregation logic used by both production main() and automated tests.
    """
    all_lengths = []
    total_words = 0
    total_sentences = 0
    total_gt_28 = 0

    for r in results:
        all_lengths.extend(r['lengths'])
        total_words += r['words']
        total_sentences += r['sentences']
        total_gt_28 += r['gt_28']

    overall_mean = (total_words / total_sentences) if total_sentences > 0 else 0.0
    overall_median = statistics.median(all_lengths) if all_lengths else 0.0
    overall_pct_gt_28 = (total_gt_28 / total_sentences * 100) if total_sentences > 0 else 0.0

    return {
        'count': len(results),
        'words': total_words,
        'sentences': total_sentences,
        'lengths': all_lengths,
        'mean': overall_mean,
        'median': overall_median,
        'gt_28': total_gt_28,
        'pct_gt_28': overall_pct_gt_28,
        'min_mean': min((r['mean'] for r in results), default=0.0),
        'max_mean': max((r['mean'] for r in results), default=0.0),
        'min_median': min((r['median'] for r in results), default=0.0),
        'max_median': max((r['median'] for r in results), default=0.0)
    }

class CorpusTokenizerTests(unittest.TestCase):
    """
    Unit tests ensuring tokenizer heuristics and aggregation behave predictably.
    """
    def test_bce_terminal(self):
        res = analyze_text('This happened in 300 B.C.E. Then it changed.')
        self.assertEqual(res['sentences'], 2)

    def test_bce_mid_sentence(self):
        res = analyze_text('In 300 B.C.E., ancient bakers used sourdough.')
        self.assertEqual(res['sentences'], 1)

    def test_ce_terminal(self):
        res = analyze_text('In 500 C.E. trade flourished. It was widespread.')
        self.assertEqual(res['sentences'], 2)

    def test_us_terminal(self):
        res = analyze_text('He traveled across the U.S. Then he wrote a book.')
        self.assertEqual(res['sentences'], 2)

    def test_us_market_modifier(self):
        res = analyze_text('The U.S. Market expanded rapidly.')
        self.assertEqual(res['sentences'], 1)

    def test_eg_sentence_end(self):
        res = analyze_text('Use a stabilizer, e.g. Then test again.')
        self.assertEqual(res['sentences'], 2)

    def test_eg_mid_sentence(self):
        res = analyze_text('Use a stabilizer, e.g. gelatin, for best results.')
        self.assertEqual(res['sentences'], 1)

    def test_decimals(self):
        res = analyze_text('The mixture requires 2.3 grams of salt and 10.5 ml of water.')
        self.assertEqual(res['sentences'], 1)
        self.assertEqual(res['words'], 12)

    def test_audio_tags_allowlist(self):
        text = 'The bread rises [music] slowly and [background-music] then bakes [applause] with loud cheers [snorts].'
        res = analyze_text(text)
        self.assertEqual(res['sentences'], 1)
        self.assertEqual(res['words'], 10)

    def test_semantic_brackets_retained(self):
        text = 'The chapter [Chapter 1] starts here.'
        res = analyze_text(text)
        self.assertEqual(res['sentences'], 1)
        self.assertEqual(res['words'], 6)

    def test_empty_corpus(self):
        res = analyze_text('')
        self.assertEqual(res['words'], 0)
        self.assertEqual(res['sentences'], 0)
        self.assertEqual(res['mean'], 0.0)
        self.assertEqual(res['median'], 0.0)

    def test_production_aggregation(self):
        t1 = analyze_text('Sentence one. Sentence two.')
        t2 = analyze_text('A longer third sentence for testing purposes.')

        # Test empty list
        agg_empty = aggregate_results([])
        self.assertEqual(agg_empty['count'], 0)
        self.assertEqual(agg_empty['words'], 0)
        self.assertEqual(agg_empty['mean'], 0.0)

        # Test single item
        agg_single = aggregate_results([t1])
        self.assertEqual(agg_single['count'], 1)
        self.assertEqual(agg_single['sentences'], 2)

        # Test multiple items
        agg_multi = aggregate_results([t1, t2])
        self.assertEqual(agg_multi['count'], 2)
        self.assertEqual(agg_multi['sentences'], 3)
        self.assertEqual(agg_multi['words'], 4 + 7)

def main():
    if '--test' in sys.argv:
        # Strip --test flag so unittest.main() doesn't interpret it
        sys.argv.remove('--test')
        unittest.main()
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(glob.glob(os.path.join(script_dir, 'scripts', '*.md')))

    results = [analyze_file(f) for f in files]
    summary = aggregate_results(results)

    print(f'| # | Tên Tệp | Số Từ | Số Câu | Trung Bình (Mean) | Trung Vị (Median) | Số Câu >28 từ | % Câu >28 từ |')
    print(f'|---|---|---|---|---|---|---|---|')

    for i, r in enumerate(results, 1):
        pct_gt_28 = (r['gt_28'] / r['sentences'] * 100) if r['sentences'] > 0 else 0.0
        print(f"| {i} | `{r['filename']}` | {r['words']:,} | {r['sentences']:,} | {r['mean']:.1f} | {r['median']:.1f} | {r['gt_28']} | {pct_gt_28:.1f}% |")

    print(f"| **Tổng** | **Toàn bộ Corpus ({summary['count']} video)** | **{summary['words']:,}** | **{summary['sentences']:,}** | **{summary['mean']:.1f}** | **{summary['median']:.1f}** | **{summary['gt_28']}** | **{summary['pct_gt_28']:.1f}%** |")

    print("\n--- Summary Metrics ---")
    print(f"Total Files Analyzed: {summary['count']}")
    print(f"Total Words: {summary['words']}")
    print(f"Total Sentences: {summary['sentences']}")
    print(f"Overall Mean: {summary['mean']:.2f} words/sentence")
    print(f"Overall Median: {summary['median']:.1f} words/sentence")
    if results:
        print(f"Per-Video Mean Range: {summary['min_mean']:.1f} – {summary['max_mean']:.1f}")
        print(f"Per-Video Median Range: {summary['min_median']:.1f} – {summary['max_median']:.1f}")
    print(f"Total Sentences > 28 Words: {summary['gt_28']} ({summary['pct_gt_28']:.2f}%)")

if __name__ == '__main__':
    main()
