# AI Engineering Course

A personal, structured bootcamp working through the **Free AI Engineer Course (8 weeks)** by Pratyush Narain — one lecture at a time, building everything by hand.

This repository is designed to be a **long-term learning resource**, not a dump of copied code. Every episode leaves behind working code, notes explaining *why*, and an honest record of what was hard.

**Background:** written by a C#/.NET engineer learning Python. Python concepts throughout are explained against their .NET equivalents.

---

## Start here

| File | What it's for |
|---|---|
| **[LEARNING_GUIDE.md](LEARNING_GUIDE.md)** | How we work — the teaching contract and the per-episode workflow. **Read this first.** |
| **[COURSE_PROGRESS.md](COURSE_PROGRESS.md)** | Where I am: episodes done, in progress, upcoming, and confidence per episode |
| **[LEARNING_JOURNAL.md](LEARNING_JOURNAL.md)** | Personal reflections and the rolling list of things to revisit |
| **[GLOSSARY.md](GLOSSARY.md)** | Every term, each with a C#/.NET analogy |
| **[CHEATSHEET.md](CHEATSHEET.md)** | Every command actually used, with its `dotnet` equivalent |
| **[PYTHON_GOTCHAS.md](PYTHON_GOTCHAS.md)** | Traps that specifically catch C# developers — also the source of debugging challenges |
| **[RESOURCES.md](RESOURCES.md)** | External links, consoles, documentation |

---

## Layout

```
├── Week1/ … Week8/
│   ├── week-N-review.md      # end-of-week integration review
│   └── episode-NN-short-title/
│       ├── notes.md          # what we learned and built
│       ├── source-notes.md   # the raw lecture notes, preserved unmodified
│       ├── assessment.md     # concept check, exercises, reflection — my answers
│       └── code/             # practice scripts for this episode only
├── projects/                 # applications spanning multiple episodes
├── templates/                # notes, assessment, and week review templates
└── [pyproject.toml, uv.lock, .python-version, main.py]
```

**Every episode ends with an assessment** — explain the concepts in my own words, apply them in a small exercise, and debug broken code. An episode isn't complete until it's passed. Each week closes with an integration review. See [LEARNING_GUIDE.md §5](LEARNING_GUIDE.md#5-the-episode-assessment).

**Why `notes.md` and `source-notes.md` are separate:** `source-notes.md` is what the *course* said; `notes.md` is what *I* actually did, including deviations, mistakes, and gotchas. Months from now, that distinction is the whole value.

**Why `code/` and `projects/` are separate:** `code/` holds disposable single-concept scripts; `projects/` holds real applications with their own lifecycle. See [projects/README.md](projects/README.md).

---

## Setup

Single [uv](https://docs.astral.sh/uv/) project at the root — one virtual environment shared across all weeks.

```bash
uv sync          # install dependencies into .venv
uv run main.py   # run a script inside the project's venv
```

Copy `.env.example` to `.env` and fill in real values. **`.env` is git-ignored and must stay that way.**

---

## Deviations from the course

| Course uses | We use | Why |
|---|---|---|
| Groq Cloud (LLM inference) | **OpenAI** | Existing access |
| Qdrant Cloud (vector DB) | **Azure**, deferred | Introduced when the RAG lectures need it |

---

## Progress

Week 1 in progress — see [COURSE_PROGRESS.md](COURSE_PROGRESS.md) for detail.

| Week | Theme |
|---|---|
| 1–2 | Setup & LLM fundamentals |
| 3 | RAG & document Q&A |
| 4 | AI agents |
| 5 | LangGraph |
| 6 | MCP servers |
| 7 | Observability & evaluation |
| 8 | Deployment, fine-tuning & capstone |
