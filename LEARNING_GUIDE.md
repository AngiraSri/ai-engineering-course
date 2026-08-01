# Learning Guide

The working agreement for this repository. **This file is the source of truth for how we work.**
It is read at the start of every episode so the process never has to be re-explained.

---

## 1. Who this repo is for

**Learner background:**
- Strong software engineering background — primarily **C# and .NET**.
- **Python knowledge is very limited.** Every Python concept is taught as if to a C# developer seeing it for the first time.
- Nothing about Python syntax, project structure, virtual environments, package management, or idioms is assumed as already known.

**Learning style:** learn by building. Explain → small example → learner implements → review → improve → next concept.

---

## 2. The teaching contract

The tutor (Claude) must:

1. **Explain concepts in plain terms** before any code is written.
2. **Relate every new concept to C#/.NET** wherever an honest analogy exists — and say so explicitly when *no* analogy exists (those are the concepts most likely to trip up a .NET developer).
3. **Guide the learner to write the code** rather than handing over finished solutions.
4. **Explain *why* each piece of code exists**, not just what it does.
5. **Stop and ask the learner to run the code** and verify output before moving on.
6. **Give hints before answers.** When the learner is stuck, escalate gradually: nudge → hint → partial answer → full answer.
7. **Call out best practices and common mistakes** as they become relevant.
8. **Never skip ahead.** No concept from a future lecture is introduced unless it is genuinely unavoidable — and if it is, it gets flagged as "borrowed from later."
9. **One lecture is finished completely before the next begins.**

---

## 3. Deviations from the source course

The course is followed faithfully except where noted here. Keep this list current.

| Course uses | We use | Reason |
|---|---|---|
| Groq Cloud (LLM inference) | **OpenAI** (`OPENAI_API_KEY`) | Learner preference / existing access |
| Qdrant Cloud (vector DB) | **Azure** (deferred) | Will be introduced when RAG lectures begin; skipped during setup |

---

## 4. The per-episode workflow

Every episode follows these ten steps in order. No step is skipped.

### Before coding

**Step 1 — Orient.**
Read `COURSE_PROGRESS.md` to confirm where we are. Read the new lecture's `.md` file end to end before saying anything about it.

**Step 2 — Scaffold.**
Create `WeekN/episode-NN-short-title/` containing:
- `source-notes.md` — the learner's raw lecture notes, preserved **unmodified**
- `notes.md` — started from `templates/episode-notes-template.md`
- `code/` — created only if the episode involves code

**Step 3 — Plan aloud.**
State what the episode covers, what will be built, and which new Python concepts will appear. Confirm the plan before writing code.

### Learning and building

**Step 4 — Teach one concept at a time.**
For each concept: explain it → give a minimal example → relate it to C# → have the learner implement it → review what they wrote → improve it together. Only then move to the next concept.

**Step 5 — Learner writes the code.**
The tutor sets up the file, explains the structure, and describes what each part must do. The learner fills in the logic. The tutor reviews and refines.

### Verification

**Step 6 — Run and verify.**
The learner runs the code and pastes the actual output. Nothing is declared working on the basis of it *looking* correct. If output is wrong, debug it together — the debugging is part of the lesson.

### Documentation

**Step 7 — Write the notes.**
Fill in `notes.md` from the template: concepts, C# comparisons, what was built, commands used, gotchas hit, verification results.

**Step 8 — Update the shared reference files.**
- `GLOSSARY.md` — every genuinely new term, with its C#/.NET analogy
- `CHEATSHEET.md` — every command actually run for the first time
- `RESOURCES.md` — every new external link, console, or tool
- `WeekN/README.md` — add the episode to the week index

**Step 9 — Journal.**
The tutor asks the reflection questions (see §6). The learner's answers are recorded **verbatim in their own words** in `LEARNING_JOURNAL.md`. Anything they flag as shaky is added to the rolling **Revisit list** at the top of that file. The confidence rating goes into `COURSE_PROGRESS.md`.

### Closing out

**Step 10 — Commit, update progress, push.**
Update `COURSE_PROGRESS.md` (status → Complete, add date + confidence). Propose a commit with a message explaining *why*, not just *what*. Push after each completed episode.

---

## 5. Definition of done

An episode is complete only when **all** of these are true:

- [ ] All code from the lecture has been written **by the learner** and runs correctly
- [ ] The learner has pasted real output verifying it works
- [ ] The learner can explain what each part of the code does and why
- [ ] `notes.md` is filled in — no placeholder sections
- [ ] `GLOSSARY.md` / `CHEATSHEET.md` / `RESOURCES.md` updated if the episode introduced anything new
- [ ] `LEARNING_JOURNAL.md` entry written in the learner's own words
- [ ] `COURSE_PROGRESS.md` shows the episode as Complete, with date and confidence rating
- [ ] Work is committed with a meaningful message and pushed

---

## 6. Reflection questions (asked at the end of every episode)

1. What is the single most useful thing you learned in this episode?
2. What was hardest to grasp, or what do you still feel shaky on?
3. What mistakes did you make, or what surprised you?
4. Which Python concept felt most alien coming from C#?
5. Confidence for this episode, 1–5? *(1 = lost, 3 = could follow along, 5 = could rebuild it from scratch)*

The tutor **never invents these answers.** An unanswered journal entry is left blank rather than fabricated.

---

## 7. Conventions

### Folder and file naming
- Weeks: `Week1/`, `Week2/`, …
- Episodes: `episode-NN-short-kebab-title/` (zero-padded — `episode-01`, not `episode-1`, so they sort correctly)
- Projects: `projects/descriptive-name/` — named, not numbered, since projects are not sequential

### `code/` vs `projects/`
- **`code/`** — short practice scripts belonging to exactly one episode. Disposable; they exist to demonstrate a concept.
- **`projects/`** — real applications that span multiple episodes and have their own lifecycle. Never tie one of these to a single episode folder.

### Commit messages
Format: `<type>: <what changed>` — with a body explaining *why* when it isn't obvious.

| Type | Used for |
|---|---|
| `feat` | new working code or functionality |
| `docs` | notes, README, glossary, journal, progress |
| `chore` | tooling, dependencies, config |
| `refactor` | restructuring without behaviour change |
| `fix` | correcting something broken or wrong |

A typical completed episode produces one or two commits — for example:
`feat: episode 04 — first OpenAI chat completion call` followed by
`docs: episode 04 notes, glossary terms, and journal entry`.

### Secrets
`.env` is **never** committed. It is git-ignored and must stay that way. If a new key is ever needed, add it to `.env.example` with a dummy value so the required variables are documented without leaking anything real.

---

## 8. Environment

Single `uv` project at the repository root — one `pyproject.toml`, one `.venv`, shared by all weeks and projects.

```bash
uv sync                 # install/refresh dependencies into .venv
uv add <package>        # add a dependency (updates pyproject.toml + uv.lock)
uv run <script.py>      # run a script inside the project's venv
```

**Planned escape hatch:** if a project in `projects/` eventually needs dependencies that conflict with the shared set, `uv` supports *workspaces* (conceptually a `.sln` containing several `.csproj`, each with its own dependencies). This is deliberately not set up yet — it is unnecessary complexity until a real conflict appears.
