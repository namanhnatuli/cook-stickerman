#!/usr/bin/env python3
"""
Reproducible Corpus Analysis Script for cook-stickerman benchmark transcripts.

Methodology & Rules:
1. Strips non-spoken audio tags (e.g., '[music]').
2. Replaces common decimal points (e.g., '120° C', '2.3 million') so numbers don't split sentences.
3. Protects common abbreviations (e.g., 'vs.', 'B.C.E.', 'U.S.').
4. Splits sentences on standard terminal punctuation: '.', '!', '?'.
5. Filters out empty sentence segments.
6. Computes tokenized word count, sentence count, mean, median, and sentences exceeding 28 words.
"""

import glob
import os
import re
import statistics

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Step 1: Remove bracketed audio tags like [music]
    cleaned = re.sub(r'\[music\]', '', raw_text, flags=re.IGNORECASE)

    # Step 2: Protect decimals in numbers (e.g., "2.3 million" -> "2<DOT>3 million")
    cleaned = re.sub(r'(\d+)\.(\d+)', r'\1<DOT>\2', cleaned)

    # Step 3: Protect common abbreviations
    cleaned = re.sub(r'\b(vs|etc|dr|mr|mrs|prof|vol|no|b\.c\.e|c\.e|u\.s)\.', r'\1<ABBR_DOT>', cleaned, flags=re.IGNORECASE)

    # Step 4: Split sentences on terminal punctuation (. ! ?)
    raw_sentences = re.split(r'[.!?]+', cleaned)

    # Step 5: Clean and tokenize sentences
    sentences = []
    for s in raw_sentences:
        # Restore protected tokens
        s_restored = s.replace('<DOT>', '.').replace('<ABBR_DOT>', '.')
        words = s_restored.strip().split()
        if words:
            sentences.append(words)

    total_words = sum(len(w) for w in sentences)
    sentence_count = len(sentences)
    sentence_lengths = [len(w) for w in sentences]

    mean_len = (total_words / sentence_count) if sentence_count > 0 else 0.0
    median_len = statistics.median(sentence_lengths) if sentence_lengths else 0.0
    gt_28 = sum(1 for l in sentence_lengths if l > 28)

    return {
        'filename': os.path.basename(filepath),
        'words': total_words,
        'sentences': sentence_count,
        'lengths': sentence_lengths,
        'mean': mean_len,
        'median': median_len,
        'gt_28': gt_28
    }

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(glob.glob(os.path.join(script_dir, 'scripts', '*.md')))

    results = [analyze_file(f) for f in files]

    all_lengths = []
    total_words = 0
    total_sentences = 0
    total_gt_28 = 0

    print(f'| # | Tên Tệp | Số Từ | Số Câu | Trung Bình (Mean) | Trung Vị (Median) | Số Câu >28 từ | % Câu >28 từ |')
    print(f'|---|---|---|---|---|---|---|---|')

    for i, r in enumerate(results, 1):
        all_lengths.extend(r['lengths'])
        total_words += r['words']
        total_sentences += r['sentences']
        total_gt_28 += r['gt_28']
        pct_gt_28 = (r['gt_28'] / r['sentences'] * 100) if r['sentences'] > 0 else 0.0
        print(f"| {i} | `{r['filename']}` | {r['words']:,} | {r['sentences']:,} | {r['mean']:.1f} | {r['median']:.1f} | {r['gt_28']} | {pct_gt_28:.1f}% |")

    overall_mean = total_words / total_sentences if total_sentences > 0 else 0.0
    overall_median = statistics.median(all_lengths) if all_lengths else 0.0
    overall_pct_gt_28 = (total_gt_28 / total_sentences * 100) if total_sentences > 0 else 0.0

    print(f'| **Tổng** | **Toàn bộ Corpus (10 video)** | **{total_words:,}** | **{total_sentences:,}** | **{overall_mean:.1f}** | **{overall_median:.1f}** | **{total_gt_28}** | **{overall_pct_gt_28:.1f}%** |')

    print("\n--- Summary Metrics ---")
    print(f"Total Words: {total_words}")
    print(f"Total Sentences: {total_sentences}")
    print(f"Overall Mean: {overall_mean:.2f} words/sentence")
    print(f"Overall Median: {overall_median:.1f} words/sentence")
    print(f"Per-Video Mean Range: {min(r['mean'] for r in results):.1f} – {max(r['mean'] for r in results):.1f}")
    print(f"Per-Video Median Range: {min(r['median'] for r in results):.1f} – {max(r['median'] for r in results):.1f}")
    print(f"Total Sentences > 28 Words: {total_gt_28} ({overall_pct_gt_28:.2f}%)")

if __name__ == '__main__':
    main()
