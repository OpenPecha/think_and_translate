# Evaluation & Results

## Overview

Through our work with *Melong*, we've found that breaking down machine translation into smaller, reasoning-driven tasks significantly enhances output quality compared to direct translation. This method mirrors how human translators approach their work, making the process more intuitive and aligned with human thought patterns.

**Try it yourself**: [DEMO](https://huggingface.co/spaces/openpecha/Translation_TPO_demo)

> ⚠️ This is a proof of concept. The model may occasionally repeat itself—click stop if that happens.

---

## The OpenAI o1 Inspiration

Hyung Won at OpenAI demonstrated reasoning-driven translation using a corrupted Korean sentence with unnecessary consonants:
- **GPT-4**: Failed to translate correctly
- **O1**: Deciphered → Reasoned → Translated accurately

This structured "think before translating" approach is what TPO brings to Tibetan-English translation.

---

## Metrics

| Metric | Purpose |
|--------|---------|
| **BLEURT** | Primary metric for semantic accuracy and ranking |
| **BLEU** | Checks technical term inclusion (crucial for Buddhist texts) |
| **Win Rate** | Pairwise preference comparison |

---

## Baselines

| Model | Prompt Strategy |
|-------|-----------------|
| **Claude Direct** | Simple "Please translate the following..." |
| **Claude Technical** | Act as an expert Buddhist translator |
| **Claude COT** | Expert Buddhist translator + chain-of-thought reasoning |
| **TPO** | Our reasoning-trained model |

---

## Results

### BLEURT Scores

**TPO outperforms Claude.**

![BLEURT Results](../docs/assets/bleurt_graph.png)

### BLEU Scores

BLEU shows whether technical terms are correctly included—crucial for domain-specific translations.

![BLEU Results](../docs/assets/bleu_graph.png)

### Win Rate Heatmap

Pairwise comparison of model preferences:

![Win Rate Heatmap](../docs/assets/winrate_heatmap.png)

---

## Conclusion

Using TPO for translation offers unique advantages in **interpretability**—we gain visibility into how the model understands and processes language.

Compared to non-reasoning approaches, TPO currently performs slightly less effectively. This aligns with findings from the TPO paper: **we only implemented two iterations of DPO**. With additional iterations, we anticipate TPO will outperform non-reasoning approaches.

### Key Takeaways

1. **Interpretability wins**: Users value seeing the reasoning behind translations
2. **More DPO iterations needed**: Performance expected to scale with 3-5+ iterations
3. **BLEURT > BLEU**: Semantic metrics better capture Buddhist text quality

---

## Future Directions

| Direction | Potential |
|-----------|-----------|
| **Online DPO** | Use Claude as real-time reward model |
| **Dedicated Reward Model** | Train specifically for Buddhist translation quality |
| **Extended Reasoning** | Longer reasoning steps for complex passages |
| **Reasoning Agents** | Retrieve translations, search dictionaries, consult commentaries |

> Reasoning agents could represent the ultimate solution—an agent that can reason, search, and integrate information to ensure high-quality translations.

---

**Full project details**: [OpenPecha Project Board](https://github.com/orgs/OpenPecha/projects/107/views/1?pane=issue&itemId=91865719&issue=OpenPecha%7Cthink_and_translate%7C2)
