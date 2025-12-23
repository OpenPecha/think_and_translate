# Experimental Results & Analysis

This document details the performance of the **Think then Translate (TPO)** model compared to various Claude 3.5 Sonnet baselines. For implementation tracking and discussion, see [GitHub Issue #1](https://github.com/OpenPecha/think_and_translate/issues/1).

## Evaluation Metrics

We prioritized **BLEURT** for its superior ability to evaluate semantic similarity and coherence in complex Buddhist texts.

| Metric | Purpose |
| :--- | :--- |
| **BLEURT** | Primary metric for semantic accuracy and ranking. |
| **BLEU** | Verification of technical term inclusion and local n-gram matching. |
| **Win Rate** | Pairwise comparison of model preferences. |

## Comparative Performance

We evaluated the TPO model against four configurations:
1.  **Claude Direct**: Standard translation prompt.
2.  **Claude Technical**: Prompted as an expert Buddhist translator.
3.  **Claude COT**: Expert Buddhist translator with reasoning steps.
4.  **TPO (Monlam Melong)**: Our reasoning-driven model.

### BLEURT Analysis
Our experiments indicate that TPO outperforms Claude Direct and remains competitive with specialized technical prompts.

![BLEURT Results](https://github.com/OpenPecha/think_and_translate/raw/main/docs/assets/bleurt_graph.png) *(Note: Placeholder path for graph)*

### BLEU Analysis
BLEU was utilized to ensure technical terms were correctly included.

![BLEU Results](https://github.com/OpenPecha/think_and_translate/raw/main/docs/assets/bleu_graph.png) *(Note: Placeholder path for graph)*

### Win Rate Heatmap
The win rate analysis reveals that while non-reasoning approaches are currently performing slightly more effectively, the TPO approach provides unique interpretability and "reasoning wins" on complex corrupted text.

![Win Rate Heatmap](https://github.com/OpenPecha/think_and_translate/raw/main/docs/assets/winrate_heatmap.png) *(Note: Placeholder path for graph)*

## Implementation Details (PMA0015)

The project followed a structured implementation path as outlined in [GitHub Issue #1](https://github.com/OpenPecha/think_and_translate/issues/1):
- **Thought Generation**: Integrated reasoning before producing final translations.
- **DPO Training**: Conducted two iterations of Direct Preference Optimization (DPO 1 & DPO 2).
- **Interpretability**: Gained visibility into the model's understanding of language—a feature highly valued by our users.

## Conclusion & Insights
TPO currently performs slightly less effectively than optimized non-reasoning approaches due to having only two DPO iterations. However, we anticipate that additional DPO cycles and online DPO using Claude as a reward model will push TPO performance beyond direct translation baselines.

