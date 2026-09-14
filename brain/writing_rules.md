# EDITORIAL HANDBOOK & VOICE CODEX FOR YOUTUBE EXPLAINERS
*An evidence-based editorial framework categorizing transcript observations, brand voice decisions, factual integrity standards, YouTube policy realities, and production heuristics.*

---

## SECTION A: FACTUAL INTEGRITY STANDARDS (NON-NEGOTIABLE)

1. **Zero Hallucination Mandate:**
   - Never fabricate or invent dates, inventor names, corporate campaigns, chemical mechanisms, or historical anecdotes.
   - If any claim, number, or connection is unverified, leave it blank or explicitly mark it with **`[NEEDS VERIFICATION]` / `[CẦN KIỂM CHỨNG]`**. Never invent facts to fill a narrative gap.

2. **Claim-Status Integrity:**
   - Use only claims supported by the Verified Research Dossier.
   - Claims marked `[CONFIRMED]` must be stated factually.
   - Claims marked `[DISPUTED]` must be explicitly framed as contested (e.g., *"Both Mexico and Nicaragua claim its origin..."*).
   - Claims marked `[POPULAR MYTH]` must be explicitly identified as folklore, marketing campaigns, or unverified popular beliefs.
   - Never narrate claims marked `[UNVERIFIED - DO NOT NARRATE]`.

3. **Causal Chain Rigor:**
   - Every explained item must convey an authentic causal chain: `[Technique / Ingredient Choice]` → `[Physical / Chemical Mechanism]` → `[Visible Crumb / Texture Outcome]` → `[Baker Takeaway]`.
   - Signposted inferences are permitted only when they follow directly from verified physical properties documented in the dossier (e.g., oil remaining liquid at refrigerated temperatures). Do not introduce new factual claims via inference.

4. **Justified Precision (Anti-False Precision):**
   - Use exact numbers, temperatures, dates, and locations only when they are directly supported by the research dossier and scientifically justified.
   - When exact figures vary or are unmeasured, use sourced ranges (e.g., *"between 90°C and 95°C depending on hydration"*) rather than inventing false precision (e.g., declaring *"exactly 93.4°C"*).

---

## SECTION B: PLATFORM POLICY REALITIES (BASED ON OFFICIAL YOUTUBE GUIDELINES)

1. **Context-Based Safety Rule (Overriding Keyword Blacklists):**
   - Ordinary culinary and educational references to knives, blades, cutting, heat, flames, or minor oven burns are **not** automatic policy violations. YouTube evaluates whether content sensationally focuses on violence, gore, or dangerous activities.
   - Do not replace ordinary culinary terms with bizarre euphemisms (e.g., do not write *"lost crimson pigment"* instead of explaining a historical injury, and do not call a chef's knife a generic *"cutting instrument"* when *"baker's knife"* or *"bread knife"* is natural).
   - Never distort historical or scientific meaning merely to avoid a benign keyword.

2. **Graphic & Sensitive Content Handling:**
   - Flag content only when it graphically or sensationally focuses on gore, severe injury, self-harm, suicide, or dangerous acts easily imitated by minors.
   - When covering tragic historical events (famine, wartime rationing, industrial accidents like the Boston Molasses Flood), use a calm, respectful documentary context without gratuitous dramatization.

3. **Altered & Synthetic Content Disclosure (Official YouTube GenAI Policy):**
   - `writing_rules.md` is the unified source of truth for all platform and editorial disclosure decisions across the pipeline.
   - **Platform Disclosure Required (YouTube Studio Toggle: YES):**
     - *AI-Generated Music / Soundtrack:* Requires disclosure if video uses generative AI to synthesize the soundtrack or background musical composition.
     - *Voice Cloning of Other Individuals:* Requires disclosure if voice cloning or voice conversion technology mimics a real living or historical person saying words they did not speak.
     - *Photorealistic Synthetic Media:* Requires disclosure if realistic/photorealistic footage or images depict real people doing things they didn't do, or realistically portray real-world events that did not occur.
   - **Platform Disclosure NOT Required (YouTube Studio Toggle: NO):**
     - *Creator's Own Voice Clone:* Does not require disclosure when narrating original educational content in the creator's authorized voice.
     - *Stylized 2D Animation & Mascots:* Cook Stickerman 2D character overlays, animated icons, and standard motion graphics do not require platform disclosure.
   - **Conditional Assessment (Generic Synthetic TTS):**
     - Standard generic text-to-speech narration reading original educational scripts does not require platform disclosure unless it impersonates a recognizable real individual, depicts synthetic events deceptively, or creates realistic confusion. Generic TTS must be evaluated on this conditional basis rather than blindly grouped with personal voice clones.
   - **Epistemic Clarity Label:** When an educational cross-section diagram or 3D cutaway is conceptual rather than a physical microscopic scan, add an on-screen label (*"Illustrative model / Concept diagram"*) to maintain educational rigor.

---

## SECTION C: CHANNEL EDITORIAL DECISIONS & BRAND VOICE

1. **Narrator Persona (The Observant Specialist):**
   - Calm, observant, curious, and authoritative without arrogance.
   - The voice of an experienced baker and food scientist who finds the physical mechanisms of everyday foods genuinely fascinating.
   - Avoid frantic, over-caffeinated YouTube delivery or dry academic lecturing.

2. **Point of View & Perspective:**
   - **Third-Person Objective (85–90%):** The subject of the sentence should be the cake, the protein, the gas bubble, or the historical baker (*"The batter expands...", "Heat moves inward...", "Bakers in the 1920s realized..."*).
   - **Second-Person ("You"):** Use intentionally when placing the viewer in the physical kitchen experience or sensory moment (*"When you slice into the crust...", "If you notice the center sinking..."*).
   - **First-Person ("I / Me"):** Banned in the explanatory body. The narrator does not inject personal ego.
   - **First-Person Plural ("We / Us"):** Permitted in the outro or during a synthesis transition (*"Now that we've seen how foam cakes trap air..."*).

3. **Call-to-Action (CTA) Philosophy:**
   - **Standard Baseline:** Normally **zero or one concise, thoughtful CTA in the outro** (inviting comments on texture preferences or suggesting the next topic). Include it only when it creates a natural, valuable next action for the viewer.
   - **Optional Mid-Body Question:** At most one organic diagnostic question in the explanatory body (e.g., asking if viewers have experienced a specific cake collapse), used strictly to enhance viewer engagement with the physical mechanism.
   - **Editorial Rule:** Never force CTAs to hit an arbitrary count. Benchmark analysis of 10 sampled explainers demonstrates that 6 of 10 videos contain zero CTAs. Never beg for subscriptions in the opening hook.

4. **Sensory Vocabulary (Tactile Precision):**
   - Prioritize words that convey physical mouthfeel, crumb elasticity, and sound:
     - *Texture:* Brittle crack, glassy shell, pillowy rebound, tight uniform crumb, velvety mouth-coat, delicate wobble, molten center, crumbly resistance.
     - *Physics:* Coagulate, aerate, gelatinize, emulsify, steam lift, Maillard browning.
   - Avoid empty taste adjectives (*delicious, yummy, tasty, mind-blowing*). Describe the flavor components (bittersweet, caramelized, lactic tang, nutty).

---

## SECTION D: CORPUS OBSERVATIONS (PATTERNS FROM SAMPLED BENCHMARK EXPLAINERS)
*Empirical observations derived from analysis of 10 sampled culinary explainer transcripts in `research/scripts/` (see full benchmark provenance, view counts, and ASR transcription caveats in [`research/corpus_metadata.md`](../research/corpus_metadata.md)).*

> **CRITICAL DATA NOTE ON CORPUS TRANSCRIPTS:**
> The transcripts in `research/scripts/` are automated speech recognition (ASR) captures containing known phonetic errors (e.g., misheard inventor names and scrambled pastry terms). Use these scripts **strictly for structural pacing, transition mechanics, and information cadence analysis**, never as primary factual sources for baking science.


1. **Sentence Length Rhythm:**
   - Across the corpus, per-video sentence length averages range from **12.4 to 21.2 words per sentence** (overall mean: **16.4**, overall median: **16.0**).
   - Scripts maintain pacing momentum by interspersing **punch sentences (3–7 words)** (*"That's it."*, *"Heat dulls it fast."*, *"The brittle crack is the feature."*) between longer mechanical explanations (18–25 words).
   - *Sentence Length Heuristic:* Prefer splitting sentences above 28 words when syntactic load or read-aloud testing indicates comprehension difficulty or breath strain. This is a soft editorial heuristic, not a factual or compliance gate.

2. **Zero-Fluff Entry:**
   - All 10 sampled benchmark transcripts begin without a personal greeting (*"Hi guys"*) and move immediately into the subject, a counter-intuitive anomaly, or a category paradox.

3. **Natural Transition Methods:**
   - Sampled explainers avoid artificial listicle bridge phrases (*"Next up on our list..."*).
   - They rely on **The Boundary Shift** (showing how changing one ingredient ratio creates a new category; e.g., verbatim from `All Sugars Explained.md`: *"Brown sugar is essentially white sugar that either never had all its molasses removed or had molasses added back in..."*) and **The Noun Drop / The Hard Shift** (punctuating an item firmly, pausing, and stating the next subject; e.g., verbatim from `Every Famous Dessert Explained in 11 Minutes.md`: *"Move the ratio even slightly and you land in a different dessert. Tiramisu is a cold layered Italian dessert..."*).

---

## SECTION E: PRODUCTION HEURISTICS (PLANNING GUIDELINES, NOT HARD GATES)

1. **Pacing & Runtime Planning:**
   - Standard narration pacing is planned at **140–150 words per minute (WPM)**.
   - **Preferred Runtime is a planning estimate, NOT a compliance gate.**
   - If an episode exceeds preferred runtime:
     1. Retain every single Essential Insight.
     2. Trim only duplicate phrasing, tangential trivia, or low-value enrichment.
     3. Calculate actual runtime and present choices: keep as long-form, split into a two-part series, or refine in review.
   - Never sacrifice educational completeness solely to force a word count.

---

## SECTION F: PRE-EXPORT EDITORIAL CHECKLIST

1. [ ] **Factual Verifiability:** Every factual claim matches the research dossier. No unverified claims narrated.
2. [ ] **Educational Completeness:** The causal chain (`Ingredient/Technique` → `Mechanism` → `Result` → `Takeaway`) is intact for all items.
3. [ ] **Context-Based Safety:** Culinary terms (knives, heat, cutting) used accurately; sensitive history handled with neutral documentary dignity; zero bizarre euphemisms.
4. [ ] **Hook Immediacy:** Zero greetings; opens immediately on tension or insight within 15 seconds.
5. [ ] **Natural Transitions:** Zero listicle transition cliches (*"next up"*).
6. [ ] **Sensory Precision:** Tactile mouthfeel and mechanical verbs used; empty adjectives eliminated.
7. [ ] **Audience Respect:** At most one natural body question; no aggressive subscription begging in the intro.
