# Episode 01 — Course Intro + Tech Stack Setup

| | |
|---|---|
| **Week** | 1 |
| **Date completed** | 2026-08-01 |
| **Source notes** | [source-notes.md](source-notes.md) |
| **Code** | none — setup only |
| **Assessment** | [assessment.md](assessment.md) — Tier 0 |
| **Confidence** | 4 (mechanical) / 3 (conceptual) |

---

## What this episode covered

Course introduction and full development environment setup. No application code. The lecture explains the course philosophy (reverse-engineered from real AI Engineer interview questions, production-focused rather than research-focused) and then walks through installing Python, VS Code, Git, and the `uv` package manager, plus signing up for the cloud services used for LLM inference and vector storage.

---

## Concepts

### Cloud APIs vs. running models locally

**What it is:** the course deliberately uses hosted LLM APIs rather than running models locally with Ollama. Local models need substantial RAM and a capable GPU; a hosted API needs only an API key and an internet connection.

**C#/.NET analogy:** calling a hosted REST service instead of self-hosting the workload — the same trade-off as Azure OpenAI vs. running inference on your own VM. You give up control and pay per call, but you skip all the infrastructure.

**Why it matters:** every piece of code in this course will be an API client. The "AI engineering" is in the orchestration, retrieval, and evaluation *around* the model — not in running the model itself.

---

### Virtual environments

**What it is:** an isolated directory (`.venv/`) holding its own Python interpreter and packages, scoped to one project.

**C#/.NET analogy:** none that's clean — see [GLOSSARY.md](../../GLOSSARY.md#virtual-environment-venv). NuGet already isolates packages per project; Python installs globally by default, so the venv exists to prevent version conflicts between projects.

**Why it matters:** this is the single most common source of confusion for developers arriving at Python from another ecosystem. `uv run` manages the venv automatically, which hides most of the pain.

---

### Secrets in `.env`

**What it is:** a `KEY=value` text file holding API keys, excluded from version control.

**C#/.NET analogy:** `appsettings.Development.json` or .NET user-secrets.

**Why it matters:** the `.gitignore` entry has to exist *before* the first commit. Once a secret is pushed, rotating the key is the only real fix — deleting it in a later commit does not remove it from history.

---

## Python notes (for a C# developer)

| Python | C# equivalent | Notes |
|---|---|---|
| `def main():` | `static void Main()` | No return type, no braces; a colon starts the block |
| Indentation | `{ }` | Load-bearing syntax in Python, cosmetic in C# |
| `print(...)` | `Console.WriteLine(...)` | |
| `if __name__ == "__main__":` | *(none)* | Runs the block only when the file is executed directly, not when imported |
| `pyproject.toml` | `.csproj` | Project manifest |
| `uv.lock` | `packages.lock.json` | Pinned dependency versions — commit it |
| `.python-version` | `global.json` | Pins the language/SDK version |

---

## What we built

No application code this episode. What was set up:

- A `uv` project at the repository root — `pyproject.toml`, `.python-version`, `uv.lock`, and a scaffolded `main.py`
- A Git repository with a personal commit identity scoped to this repo only
- `.gitignore` excluding `.env` and `.venv/`
- The documentation structure described in [LEARNING_GUIDE.md](../../LEARNING_GUIDE.md)

The scaffolded `main.py`:

```python
def main():
    print("Hello from ai-engineering-course!")


if __name__ == "__main__":
    main()
```

---

## Commands used

```bash
# verify the toolchain
python --version    # 3.14.2
uv --version        # 0.11.29
git --version       # 2.52.0

# scaffold the Python project
uv init --name ai-engineering-course --no-readme

# run it — also creates .venv on first use
uv run main.py

# repo setup
git init
git config user.email "..."          # local only, not --global
git remote add origin <url>
git push -u origin master
```

Full reference: [CHEATSHEET.md](../../CHEATSHEET.md).

---

## Gotchas and mistakes

- **Nearly git-ignored `uv.lock`.** The first `.gitignore` draft excluded it. That's wrong — the lockfile is what makes the environment reproducible, exactly like `packages.lock.json`. Ignore `.venv/` (regenerable, like `bin/` and `obj/`), commit `uv.lock`.
- **The remote repo didn't need cloning.** `git init` + `git remote add origin` + `git push -u` produces the same tracking relationship `git clone` would have. This worked because the GitHub repo was empty; had it contained even a README, the histories would have diverged and a pull would have been required first.
- **The machine's global git identity is a work email.** Set a repo-local `user.email` so this personal repo commits under a personal address without disturbing the global config.
- **`LF will be replaced by CRLF` warnings** on Windows are normal line-ending normalization, not errors.

---

## Verification

- [x] Code runs without errors
- [x] Output matches what was expected
- [x] I can explain every line of what was written

**Actual output:**

```
Using CPython 3.14.2 interpreter at: C:\Users\asrivastava\AppData\Local\Python\pythoncore-3.14-64\python.exe
Creating virtual environment at: .venv
Hello from ai-engineering-course!
```

Checklist from the lecture:
- [x] `python --version` → 3.14.2
- [x] `uv --version` → 0.11.29
- [x] `git --version` → 2.52.0
- [x] `.env` contains an unquoted API key

---

## Deviations from the course

| Course | Us | Why |
|---|---|---|
| Groq Cloud for LLM inference | **OpenAI** (`OPENAI_API_KEY`) | Existing access/preference |
| Qdrant Cloud for vector DB | **Azure**, deferred | Will be set up when the RAG lectures need it — no value provisioning it now |
| Python 3.12 / 3.14.6 shown | Python 3.14.2 | Already installed; no relevant difference |

---

## Terms added to the glossary

[`venv`](../../GLOSSARY.md#virtual-environment-venv) ·
[`uv`](../../GLOSSARY.md#uv) ·
[`pyproject.toml`](../../GLOSSARY.md#pyprojecttoml) ·
[`uv.lock`](../../GLOSSARY.md#uvlock) ·
[`.python-version`](../../GLOSSARY.md#python-version) ·
[module](../../GLOSSARY.md#module) ·
[`if __name__ == "__main__":`](../../GLOSSARY.md#if-__name__--__main__) ·
[indentation as syntax](../../GLOSSARY.md#indentation-as-syntax) ·
[`.env`](../../GLOSSARY.md#env-file) ·
[API key](../../GLOSSARY.md#api-key)
