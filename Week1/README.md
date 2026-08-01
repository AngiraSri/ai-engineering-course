# Week 1

## Episode 01 — Course Intro + Tech Stack Setup

Source notes: `ai-engineer-episode-01-notes.md` (course intro, no code).

### What this episode covered
Environment setup only — no application code. Confirmed installed:
- Python 3.14.2
- uv 0.11.29 (package/dependency manager, replaces pip + venv management)
- Git 2.52.0

### Deviations
- Using **OpenAI** instead of Groq for LLM calls.
- Skipping **Qdrant**; vector DB will be Azure-based, added later.

### What we set up
- Initialized this repo (`git init`), personal identity scoped to this repo only via local `git config user.email`/`user.name` (separate from the global work identity).
- Created a single `uv` project at the workspace root (`uv init`) — one `pyproject.toml`/`.venv` shared across all weeks.
- `.gitignore` excludes `.env` (secrets) and `.venv/` (regenerable), but keeps `uv.lock` (like a NuGet lockfile — pins exact dependency versions for reproducibility).

### Concepts learned (Python vs C#)
- **Virtual environment (venv):** an isolated Python install + package set per project. Needed because, unlike NuGet, Python packages install globally by default and can clash across projects.
- **`pyproject.toml`:** project manifest, similar role to a `.csproj`.
- **Indentation is syntax:** Python has no `{ }` for blocks — indentation defines scope.
- **`if __name__ == "__main__":`:** guards code so it only runs when the file is executed directly, not when imported as a module elsewhere. No direct C# equivalent.

### Verified
- [x] `python --version`
- [x] `uv --version`
- [x] `git --version`
- [x] `.env` contains `OPENAI_API_KEY` (unquoted)
- [x] `uv run main.py` → prints `Hello from ai-engineering-course!`
