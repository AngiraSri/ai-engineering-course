# AI Engineering Course

Following the "Free AI Engineer Course" (8 weeks) by Pratyush Narain, implemented lecture by lecture.

## Deviations from the course

- **LLM provider:** OpenAI (`OPENAI_API_KEY`) instead of Groq.
- **Vector DB:** Qdrant skipped for now; will revisit with Azure when we reach the RAG lectures.

## Project setup

This is a single [uv](https://docs.astral.sh/uv/) Python project covering all weeks.

```bash
uv sync          # install dependencies into .venv
uv run main.py   # run the entry-point script
```

Python version is pinned in `.python-version`. Dependencies are declared in `pyproject.toml` and locked in `uv.lock` (commit both, never commit `.venv/` or `.env`).

## Structure

```
Week1/   # Episode notes + code for week 1
```

## Weekly notes

- [Week 1](Week1/README.md)
