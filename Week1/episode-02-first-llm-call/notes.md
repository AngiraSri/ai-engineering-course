# Episode 02 — Understand Your First LLM Call

| | |
|---|---|
| **Week** | 1 |
| **Date completed** | 2026-09-14 |
| **Source notes** | [source-notes.md](source-notes.md) |
| **Code** | [code/](code/) |
| **Assessment** | [assessment.md](assessment.md) — Tier 2 |
| **Confidence** | 4 |

---

## What this episode covered

The first real LLM API call: authenticate with a key, build a messages list, send it, parse the reply. Plus the theory behind each piece — why messages are a *list*, what the three roles are for, why the reply lives under `choices[0]`, and what tokens cost. The lecture's second half is a hands-on script of ~30 lines.

---

## Concepts

### An API call is just an HTTP request with four parts

**What it is:** an API key (authentication), a client object (the connection), a model identifier (which brain), and a messages list (the conversation).

**C#/.NET analogy:** a typed service client — construct once with credentials, call many times. `client = OpenAI(api_key=...)` is an `HttpClient` wrapper in all but name.

**Why it matters:** there is no magic here. Everything in the rest of this course is orchestration *around* this call.

---

### Statelessness — the messages list *is* the conversation

**What it is:** the API remembers nothing between calls. To continue a conversation you resend its entire history every time.

**C#/.NET analogy:** a stateless REST endpoint vs. one backed by session state. You've made this trade before; the difference is that here the resent state is *metered*.

**Why it matters:** the model generates; **your application owns the memory** — what to keep, drop, summarise, and whose conversation is whose. That split is the foundation of the agent work in Weeks 4–5. It also means cost grows quadratically with conversation length if you do the naive thing.

---

### Roles give the model the ability to resolve references

**What it is:** every message carries `system` (standing behavioural instructions), `user` (the human), or `assistant` (what the model said before).

**Why it matters:** proven in `chat_with_context.py` — with history, *"What is his age?"* resolved to Kohli; the roles are how the model reconstructs who said what.

**Caution:** `system` is strong guidance, **not a security boundary**. A user message can talk a model out of its system prompt. That's prompt injection, met properly later.

---

### Tokens are the unit of cost

**What it is:** ~4 characters, or part of a word. Both directions are billed.

**Why it matters — two non-obvious things:**
1. **Structure costs tokens.** A 5-word question billed 14 prompt tokens; the chat format's role markers are the rest.
2. **Output is the expensive side** — typically ~4× input per token, and replies are usually far longer than prompts. The main cost lever is constraining how much the model *says*, not trimming what you ask.

Measured across the two runs of `chat_with_context.py`: prompt tokens went 30 → 72 purely from adding conversation history.

---

### Knowledge cutoff — and why it's worse than "the data is old"

**What it is:** the date after which the model has seen no training data.

**Why it matters:** it does not reliably tell you when it's out of date. See the gotcha below — this episode produced a live example of the model being confidently, silently wrong.

Two distinct gaps, both closed by retrieval (Week 3):

| Gap | Example |
|---|---|
| **Temporal** — happened after training | "Who won last night?" |
| **Private** — never in training at all | "What's in our contract with Acme?" |

---

## Python notes (for a C# developer)

| Python | C# equivalent | Notes |
|---|---|---|
| `import os` | `using System;` | Whole module; call as `os.getenv(...)` |
| `from dotenv import load_dotenv` | `using static` | Pulls one name into scope |
| `{"role": "user"}` | `new Dictionary<string, string> { ... }` | Keys are **unchecked runtime strings** |
| `[message]` | `new List<T> { message }` | Zero-based indexing, same as C# |
| `create(model=..., messages=...)` | Named arguments | Idiomatic in Python, not exceptional |
| `raise ValueError(...)` | `throw new ArgumentException(...)` | `raise`, not `throw` |
| `if not api_key:` | `string.IsNullOrEmpty(apiKey)` | **Truthiness** — no direct equivalent |
| `f"text {value}"` | `$"text {value}"` | Interpolated string |
| `"""docstring"""` | `/// <summary>` | Module/function documentation |

---

## What we built

```
code/
├── hello_llm.py            # single-turn call: key → client → message → response
└── chat_with_context.py    # system prompt + multi-turn history proving context works
```

`hello_llm.py` walks the four parts of a call end to end and prints `usage`.

`chat_with_context.py` adds a `system` message constraining output to one sentence, then sends a fabricated conversation (`user` → `assistant` → `user`) so the final question *"What is his age?"* has something to refer to.

Note `chat_with_context.py` uses `OpenAI()` with no arguments — the SDK reads `OPENAI_API_KEY` from the environment itself once `load_dotenv()` has run.

---

## Commands used

```bash
# add dependencies — updates pyproject.toml AND uv.lock
uv add openai python-dotenv

# run a script inside the project venv
uv run "Week1/episode-02-first-llm-call/code/hello_llm.py"
```

---

## Gotchas and mistakes

- **Asked for 2 packages, got 18.** `openai` pulled in `httpx`, `pydantic`, `certifi` and 13 more transitively. A concrete demonstration of why `uv.lock` (exact versions, including packages you never chose) is committed while `pyproject.toml` only records the 2 you asked for — as a *range*, `openai>=2.52.0`, not a pin.
- **`openAI_key` → `api_key`.** C# camelCase leaking into Python. Convention is `snake_case` ([PEP 8](https://peps.python.org/pep-0008/)).
- **Identifying a bug ≠ fixing it.** In the debugging challenge, all 5 bugs were found — including the deliberate error of *omission* that would have been missed a week earlier — but the first fix introduced 3 new defects, including `messages = [messages]` (a `NameError`; valid syntax, runtime failure) and silently dropping the very validation that had just been identified as missing. Second pass was clean. **Run the fix.**
- **🔴 The model confidently returned a wrong age.** Asked Kohli's age *with* correct conversational context, it recalled his birthdate correctly, computed against its own frozen sense of "now," and answered **"34 years old as of now"** — wrong by three years, with no hedge. The same model had politely announced its cutoff an hour earlier in `hello_llm.py`. **It does not reliably flag its own staleness**, and anything it *derives* from a fact inherits the staleness while sounding exactly as confident as a correct answer.

Full detail in [PYTHON_GOTCHAS.md](../../PYTHON_GOTCHAS.md) and [GLOSSARY.md](../../GLOSSARY.md#knowledge-cutoff).

---

## Verification

- [x] Code runs without errors
- [x] Output matches what was expected
- [x] I can explain every line of what was written

**`hello_llm.py`:**

```
As of my last update in October 2023, Virat Kohli, the former captain of the Indian
cricket team and one of the world's top batsmen, has continued to be an influential
figure in cricket. [...]
CompletionUsage(completion_tokens=145, prompt_tokens=14, total_tokens=159, ...)
```

**`chat_with_context.py` — without history (30 prompt tokens):**

```
Virat Kohli is a highly successful Indian cricketer known for his aggressive batting
style and numerous records in international cricket.
```

**`chat_with_context.py` — with history (72 prompt tokens):**

```
Virat Kohli was born on November 5, 1988, making him 34 years old as of now.
```

Context works — *"his"* resolved to Kohli without being told who "he" was. The age is wrong; see gotchas.

---

## Deviations from the course

| Course | Us | Why |
|---|---|---|
| Groq SDK (`from groq import Groq`) | **OpenAI SDK** | Provider choice from Ep 01 |
| `llama-3.3-70b-versatile` | **`gpt-4o-mini`** | Matching provider; cheap and sufficient |
| `uv init day_1` + `uv venv env --python 3.11` per day | **Nothing** — root project reused | One project for the whole course, decided in Ep 01 |
| Copy `.env` into the episode folder | **Kept one `.env` at the root** | `load_dotenv()` walks *up* the tree and finds it. Copying secrets into multiple folders is how one eventually gets committed |
| Activate venv, then `python script.py` | **`uv run script.py`** | Handles the venv automatically |

*Also noted: the lecture's own setup commands are inconsistent — it creates a venv named `env` but then activates `.venv`. Published material has bugs too.*

---

## Terms added to the glossary

[token](../../GLOSSARY.md#token) ·
[prompt vs completion tokens](../../GLOSSARY.md#prompt-tokens-vs-completion-tokens) ·
[knowledge cutoff](../../GLOSSARY.md#knowledge-cutoff) ·
[statelessness](../../GLOSSARY.md#statelessness) ·
[roles](../../GLOSSARY.md#roles-system-user-assistant) ·
[`choices` and `n`](../../GLOSSARY.md#choices-and-the-n-parameter) ·
[client (SDK)](../../GLOSSARY.md#client-sdk)
