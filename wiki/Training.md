# Training

## Phase 1: Supervised Fine-Tuning (SFT)

**Objective**: Train model to generate `<t>reasoning</t>` before translation.

**Data Format**:
```
Input: [Tibetan Source]
Output: <t>[Reasoning]</t> [English Translation]
```

**Difficulty Scaling**:
- Simple texts → Short, direct reasoning
- Complex texts → Elaborate, multi-step reasoning

## Phase 2: Candidate Generation

**Method**: Temperature sampling at inference to generate diverse translations.

**Output**: Multiple (Source, Reasoning, Translation) candidates per input.

## Phase 3: Ranking

**BLEURT Judging** (`Judges.py`):
- Compare candidates against ground truth
- Select best (Chosen) and worst (Rejected)

**Claude ELO** (optional):
- Head-to-head comparisons via Claude
- Statistical ELO ranking

## Phase 4: Direct Preference Optimization (DPO)

**Iterations Completed**: 2

| Iteration | Dataset | Result |
|-----------|---------|--------|
| DPO 1 | Initial chosen/rejected pairs | Improved alignment |
| DPO 2 | Re-ranked pairs from DPO 1 model | Further refinement |

**Key Insight**: DPO optimizes both reasoning quality AND translation accuracy together.

