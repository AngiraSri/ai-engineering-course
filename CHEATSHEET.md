# Command Cheat Sheet

Commands actually used in this course, with what they do and the closest `dotnet`/.NET equivalent.
Added to as new commands come up — nothing here is aspirational, everything has been run at least once.

---

## uv (Python project & packages)

| Command | What it does | .NET equivalent |
|---|---|---|
| `uv init --name <name>` | Scaffold a new project (`pyproject.toml`, `.python-version`, `main.py`) | `dotnet new console` |
| `uv run <script>.py` | Run a script inside the project's venv, creating the venv first if needed | `dotnet run` |
| `uv sync` | Install/refresh dependencies into `.venv` to match the lockfile | `dotnet restore` |
| `uv add <package>` | Add a dependency — updates `pyproject.toml` **and** `uv.lock` | `dotnet add package` |
| `uv remove <package>` | Remove a dependency | `dotnet remove package` |
| `uv --version` | Check the installed uv version | `dotnet --version` |

**Note:** you rarely need to "activate" the venv manually. `uv run` handles it. That differs from older Python tutorials that tell you to run `.venv\Scripts\activate` first.

---

## Python

| Command | What it does |
|---|---|
| `python --version` | Check the installed Python version |
| `python <script>.py` | Run a script with the *system* Python — **usually not what you want** in this repo; prefer `uv run` so it uses the project's venv |

---

## Git — everyday

| Command | What it does |
|---|---|
| `git status` | What's changed, staged, and untracked |
| `git status --short` | Same, condensed — good for a quick scan |
| `git add -A` | Stage everything (respecting `.gitignore`) |
| `git add <file>` | Stage one file |
| `git commit -m "message"` | Commit staged changes |
| `git log --oneline` | Compact commit history |
| `git push` | Push to the tracked remote branch |
| `git diff` | Unstaged changes |
| `git diff --staged` | Changes that *are* staged — worth reviewing before every commit |

---

## Git — setup (one-time, already done)

| Command | What it does |
|---|---|
| `git init` | Create a new local repository |
| `git remote add origin <url>` | Point the local repo at a remote. Just records a URL — nothing is contacted yet |
| `git remote -v` | Show configured remotes |
| `git push -u origin master` | First push; `-u` sets up branch tracking so later pushes are just `git push` |
| `git config user.email "..."` | Set commit identity **for this repo only** (no `--global`) — used here to commit with a personal email while the machine's global identity is a work one |
| `git config --global --list` | Show global config |
| `git config --list --local` | Show this repo's config |

**Cloning is not required to push to a remote.** `git init` + `git remote add` + `git push -u` achieves the same setup manually — cloning simply does those steps for you *and* downloads existing history. This works cleanly only when the remote repo is empty; otherwise the histories diverge and you must pull first.

---

## Git — restructuring

| Command | What it does |
|---|---|
| `git mv <old> <new>` | Move/rename a tracked file so git records it as a **rename** (`R` in status) rather than a delete + add, preserving file history |

---

## Windows / shell notes

- Paths containing spaces must be quoted: `cd "C:\...\Baisc AI Learning"`.
- Git on Windows warns `LF will be replaced by CRLF` — this is normal line-ending normalization, not an error.
