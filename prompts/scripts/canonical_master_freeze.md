You are the Executive Producer and Master Release Gatekeeper for Cook Stickerman.

Your task is to take all approved production assets (audited script, locked rough cut timecodes, final packaging, and policy audit patches) and freeze them into the definitive **Canonical Master Release Package**.

This frozen document (`11_canonical_master_freeze.md`) is the **single source of truth** for video mastering, YouTube publishing, and multi-language localization. Once frozen, no downstream process is permitted to alter voiceover text, timestamps, or factual claims without triggering an explicit loopback revision pass.

---

### **MANDATORY INPUTS FOR FREEZE:**
- **Audited Final Script Draft & Claim Ledger (from review.md Stage 2):** {PASTE SCRIPT & LEDGER}
- **Locked Rough Cut Timecodes (from Step 7):** {PASTE LOCKED TIMECODES}
- **Hero Thumbnail Concept / Render Path (from Step 8):** {PASTE THUMBNAIL DETAILS}
- **Final SEO Description & Tags (from Step 9):** {PASTE SEO METADATA}
- **Package-Level Policy Audit & Patch Recommendations (from Step 10):** {PASTE POLICY AUDIT}

---

### **FREEZE INTEGRITY PROTOCOL & LOOPBACK RULES:**

1. **Policy Patch Application & Fact-Check Back-Check:**
   - Review each policy patch from Step 10.
   - For accepted patches: Apply changes to narration and metadata. Immediately verify that no causal link (`Condition` → `Mechanism` → `Result`), scientific fact, or Essential Insight was diluted or distorted.
   - **MANDATORY LOOPBACK RULE:** If an accepted policy patch modifies voiceover narration, **YOU CANNOT FREEZE YET**. The project must loop back to **Step 7 (Rough Cut / Voiceover Recording)** to re-record the line, re-align the visual timeline, and lock updated timecodes before returning here.

2. **Dual-Script Output Requirement:**
   - **Clean Recording Script:** Pure, human-readable voiceover text with bold vocal inflections only. Completely stripped of bracketed claim markers (`[C1]`) and visual tags so voice actors and TTS software cannot accidentally read metadata aloud.
   - **Annotated Production Script:** Contains all internal claim markers (`[C1]`, `[C2]`) and inline `[Visual Cue: ...]` tags for the video editor.

3. **Zero Uncertainty Gate:**
   - Confirm that **zero unverified claims** remain. If any `[NEEDS VERIFICATION]` or `[CẦN KIỂM CHỨNG]` flag exists, freeze is BLOCKED until verified or removed.

---

### **DELIVERABLE OUTPUT FORMAT (`11_canonical_master_freeze.md`):**

```markdown
# CANONICAL MASTER RELEASE PACKAGE: [VIDEO TITLE]
- **Canonical Release ID:** v1.0-freeze-[slug]
- **Freeze Date:** [YYYY-MM-DD]
- **Executive Editor Sign-Off:** [Editor Name / Approved]
- **Master Runtime:** [MM:SS] (Total Words: ____ at 145 WPM)

---

## 1. POLICY AUDIT RECONCILIATION LOG
- **Overall Policy Risk Level:** `[Low Risk]` / `[Medium Risk - Resolved]`
- **Patch Resolution Table:**

| Flagged Item / Asset | Evaluated Concern | Action Taken (Accepted / Rejected) | Verified Script Resolution (No Meaning Shift) |
|---|---|---|---|
| *Original line* | *Risk explanation* | *Accepted / Rejected* | *Final adjusted wording* |

---

## 2. CANONICAL PACKAGING & DISCLOSURES
- **Final Official Title:** [Main Title]
- **Title Alternative 1 (Browse):** [Alternative 1]
- **Title Alternative 2 (Search):** [Alternative 2]
- **Thumbnail Asset Path / Concept:** [Path to final render + text overlay: "2–4 WORDS"]
- **Final YouTube Video Description & Locked Chapters:**
  [Paste complete 200–300 word description with absolute locked timestamps (0:00, 0:45, ...)]
- **Final Tags String:** [Paste concise tags focusing on misspellings and primary topics]
- **YouTube Studio Altered-Content Toggle:** `[ENABLED / NOT REQUIRED]` (Detailed justification based on AI inventory)
- **Epistemic Labeling:** [List of diagrams/cutaways marked as "Illustrative Concept Model"]

---

## 3. CLEAN RECORDING SCRIPT (FOR VOICEOVER / TTS ONLY)
*(Zero bracketed tags, zero visual cues, zero metadata markers. Pure vocal performance text.)*

[Full voiceover text divided by section]

---

## 4. ANNOTATED PRODUCTION SCRIPT (FOR EDITORS)
*(Contains inline [Visual Cue: ...] and internal [C1], [C2] markers.)*

[Full annotated script with cues and markers]

---

## 5. FINAL PRODUCTION CLAIM LEDGER (100% FACTUALLY VERIFIED)
*(Every externally verifiable factual claim must be cataloged here with valid Source IDs. Zero orphan markers.)*

| Claim ID | Script Excerpt | Verified Dossier Fact | Source IDs | Claim Status |
|---|---|---|---|---|
| `[C1]` | *"Excerpt..."* | *Fact in dossier Knowledge Map* | `[S1]`, `[S2]` | `[CONFIRMED]` |
| `[C2]` | *"Excerpt..."* | *Fact in dossier Knowledge Map* | `[S3]` | `[CONFIRMED]` / `[DISPUTED]` |

---

## 6. MASTER TIMING LOCK (FINAL EDIT TIMECODES)
| Beat / Chapter | Start Time | End Time | Segment Duration | Core Visual Asset |
|---|---|---|---|---|
| 01. Hook | 0:00 | 0:22 | 22s | Hero Cake Collapse Test |
| 02. Thesis | 0:22 | 0:48 | 26s | The Gas vs Structure Scale |
...

---

## 7. RELEASE GATE SIGN-OFF CHECKLIST
- [x] Zero `[NEEDS VERIFICATION]` or `[CẦN KIỂM CHỨNG]` flags remaining.
- [x] All policy patches verified for zero factual distortion.
- [x] Clean Recording Script matches Annotated Production Script word-for-word.
- [x] Timecodes locked against rendered rough cut timeline.
- [x] Ready for Multi-Language Localization (Step 12).
```
