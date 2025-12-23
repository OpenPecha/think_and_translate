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

```
Input: "བྱང་ཆུབ་སེམས་དཔའ་"

Agent Reasoning:
<t>
This is a key Buddhist term. Let me check the dictionary...
[TOOL: dictionary_lookup("བྱང་ཆུབ་སེམས་དཔའ་")]
→ Result: "bodhisattva"

Now checking if there's a similar passage in translation memory...
[TOOL: translation_memory_search("བྱང་ཆུབ་སེམས་དཔའ་")]
→ Result: Found 3 similar examples...

Based on context and standard terminology, I'll translate as...
</t>

Output: "bodhisattva"
```

---

## Goal

Create the most accurate and interpretable Tibetan translation system—one that reasons, searches, and integrates knowledge like a human expert translator.
