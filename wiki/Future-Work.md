# Future Work

## Short Term

- [ ] **More DPO iterations** (3-5 total) to close performance gap
- [ ] **Longer reasoning** for complex philosophical passages
- [ ] **Fix repetition issues** in reasoning generation
- [ ] **Migrate to Gemini models** (Claude API access expiring)

---

## Medium Term

- [ ] **Online DPO**: Use Gemini as real-time reward model
- [ ] **Dedicated Reward Model**: Train specifically for Buddhist translation quality
- [ ] **Technical term enforcement**: Penalize incorrect terminology

---

## Long Term: Reasoning Agent with Tools

### Architecture

Build a translation agent that can pause during reasoning to access external knowledge sources.

```
┌─────────────────────────────────────────────────────────┐
│                    TRANSLATION AGENT                     │
│                                                         │
│  Source Text → [REASONING] → Tool Calls → Translation  │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   VECTOR DATABASE                        │
│                                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │ Translation │ │ Commentaries│ │  Dictionary │       │
│  │   Memory    │ │             │ │             │       │
│  └─────────────┘ └─────────────┘ └─────────────┘       │
│                                                         │
│  Filter by: function_type = "tm" | "commentary" | "dict"│
└─────────────────────────────────────────────────────────┘
```

### Agent Tools

| Tool | Purpose | Filter |
|------|---------|--------|
| **Translation Memory** | Retrieve similar translation examples | `function_type = "tm"` |
| **Commentaries** | Explain philosophical concepts and context | `function_type = "commentary"` |
| **Dictionary** | Look up standardized terminology | Direct lookup (no vector search) |

### How It Works

1. **Single Vector DB**: All sources stored together with metadata tags
2. **Filtered Retrieval**: Agent queries with filter (e.g., "find similar translations" → filter by TM)
3. **Agent Decides**: Model chooses which tool to call based on the translation challenge:
   - Unknown term → Dictionary
   - Complex philosophy → Commentaries
   - Similar sentence seen before → Translation Memory

### Example Agent Flow

**Input:** སེམས་ཙམ་དུ་སྨྲ་བའི་ལྟ་བས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གཏན་ལ་ཕབ་པ།

```
Agent Reasoning:
<t>
This passage discusses a philosophical view. I see "སེམས་ཙམ" and "ཀུན་གཞི་རྣམ་པར་ཤེས་པ" 
which are technical Cittamātra terms.

Let me check the dictionary for standard renderings...
[TOOL: dictionary_lookup("སེམས་ཙམ")]
→ "Mind-Only" / "Cittamātra"

[TOOL: dictionary_lookup("ཀུན་གཞི་རྣམ་པར་ཤེས་པ")]
→ "ālayavijñāna" / "foundation consciousness" / "storehouse consciousness"

Multiple options for ཀུན་གཞི་རྣམ་པར་ཤེས་པ. Let me check how 84000 translated similar passages...
[TOOL: translation_memory("ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གཏན་ལ་ཕབ", filter="tm")]
→ Found: "...established the ālayavijñāna..." (Saṃdhinirmocana Sūtra)
→ Found: "...affirming the foundation consciousness..." (Laṅkāvatāra)

84000 uses "ālayavijñāna" in philosophical contexts. But what does "གཏན་ལ་ཕབ་པ" 
mean here—"established" or "determined"? Let me check commentaries...
[TOOL: commentary_search("སེམས་ཙམ་གཏན་ལ་ཕབ", filter="commentary")]
→ Mipham's commentary: "གཏན་ལ་ཕབ་པ་ here means to definitively establish 
   through reasoning, not merely to assert..."

So the passage is about how the Mind-Only view *establishes* (proves) 
the ālayavijñāna through philosophical reasoning.
</t>

Output: "The Mind-Only proponents' view establishes the ālayavijñāna."
```

This example shows the agent:
1. Using **Dictionary** for standardized terms
2. Using **Translation Memory** to match 84000's conventions
3. Using **Commentaries** to resolve ambiguity in meaning

---

## Goal

Create the most accurate and interpretable Tibetan translation system—one that reasons, searches, and integrates knowledge like a human expert translator.
