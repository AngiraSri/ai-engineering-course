# Glossary

Every term encountered in this course, defined once, with a C#/.NET analogy where an honest one exists.

Terms are added as they are genuinely introduced — this file deliberately does **not** run ahead of the lectures.
Where a term has been *mentioned* but not yet taught in depth, it is marked *(not yet covered in depth)*.

---

## Python & tooling

### Virtual environment (`venv`)
An isolated directory containing its own Python interpreter and its own installed packages, scoped to a single project. Lives in `.venv/` and is never committed.

**C#/.NET analogy:** no clean equivalent — and this is exactly why it trips up .NET developers. NuGet already scopes packages per project, so isolation is automatic. In Python, packages install *globally* by default, so two projects needing different versions of the same library will conflict. A venv exists to prevent that.

**Why it matters:** every Python project you touch will assume one exists. Running code outside its venv is a common cause of "it works on my machine."

---

### `uv`
A fast Python package and project manager. Handles dependency resolution, virtual environment creation, and script execution in one tool.

**C#/.NET analogy:** roughly the `dotnet` CLI + NuGet combined. `uv add` ≈ `dotnet add package`; `uv sync` ≈ `dotnet restore`; `uv run` ≈ `dotnet run`.

**Why it matters:** it replaces the older, clunkier `pip` + `venv` + `requirements.txt` workflow. It also creates the venv automatically, so you rarely manage one by hand.

---

### `pyproject.toml`
The project manifest. Declares the project name, version, required Python version, and its dependencies.

**C#/.NET analogy:** the `.csproj` file.

---

### `uv.lock`
A lockfile pinning the exact resolved version of every dependency (including transitive ones), so the environment is reproducible on any machine.

**C#/.NET analogy:** `packages.lock.json`.

**Why it matters:** **commit this file.** `pyproject.toml` says "I need library X"; `uv.lock` says "specifically version 1.4.2, and here are its dependencies too." Without it, two people running `uv sync` a month apart can get different environments.

---

### `.python-version`
A one-line file pinning which Python version this project uses.

**C#/.NET analogy:** `global.json` pinning the SDK version.

---

### Module
Any single `.py` file. Importing it makes its functions and variables available in another file.

**C#/.NET analogy:** loosely a class file, but there is no enclosing class — a Python file can hold bare functions and variables at the top level, which C# does not allow.

---

### `if __name__ == "__main__":`
A guard placed at the bottom of a script. The code inside it runs **only** when the file is executed directly (`python main.py`), not when the file is imported by another file.

**C#/.NET analogy:** none — this is genuinely Python-specific. The closest idea is `static void Main()` being the entry point, but the mechanism is different: in Python, *every* file is runnable *and* importable, and `__name__` is a variable Python sets to `"__main__"` only for the file you actually launched.

**Why it matters:** without the guard, importing a script would execute all of its top-level code as a side effect.

---

### Indentation as syntax
Python uses indentation to define code blocks. There are no `{ }` braces.

**C#/.NET analogy:** the braces themselves. In C# indentation is cosmetic and the compiler ignores it; in Python it is load-bearing and inconsistent indentation is a syntax error — or worse, silently changes the meaning of the code.

---

## Environment & secrets

### `.env` file
A plain-text file of `KEY=value` pairs holding configuration and secrets (API keys), kept out of source control.

**C#/.NET analogy:** `appsettings.Development.json` or user-secrets — with the same rule: never commit the one containing real values.

---

### API key
A secret string that authenticates your requests to a hosted service (here, OpenAI). Anyone holding it can spend money on your account.

**Why it matters:** treat it like a password. It belongs in `.env`, never in source code, never in a commit, never pasted into a chat or screenshot.

---

## AI engineering

*(These were named in the Episode 01 course overview but not yet taught. Definitions here are intentionally brief and will be expanded when the relevant lectures arrive.)*

### LLM (Large Language Model)
A model trained to predict and generate text, accessed here through a hosted API rather than run locally. *(not yet covered in depth)*

### Inference
Running an already-trained model to get an output from an input — as opposed to training the model. *(not yet covered in depth)*

### RAG (Retrieval-Augmented Generation)
An architecture where relevant documents are retrieved and supplied to an LLM as context, so it can answer questions about data it was never trained on. *(not yet covered in depth — Week 3)*

### Vector database
A database that stores text as numerical vectors and retrieves entries by semantic similarity rather than exact keyword match. The course uses Qdrant; **we are using Azure instead.** *(not yet covered in depth)*

### AI agent
An LLM given tools and a goal, which decides for itself which actions to take in sequence. *(not yet covered in depth — Week 4)*

### MCP (Model Context Protocol)
A standard protocol for exposing tools and data sources to an LLM. *(not yet covered in depth — Week 6)*
