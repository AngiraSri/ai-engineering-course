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
6. **Give hints before answers** — see the hint ladder in §5.
7. **Call out best practices and common mistakes** as they become relevant.
8. **Never skip ahead.** No concept from a future lecture is introduced unless genuinely unavoidable — and if it is, it gets flagged as "borrowed from later."
9. **One lecture is finished completely before the next begins.**
10. **Never fabricate the learner's words.** Assessment answers, journal entries, and confidence ratings are the learner's own. Blank is always better than invented.

---

## 3. Deviations from the source course

| Course uses | We use | Reason |
|---|---|---|
| Groq Cloud (LLM inference) | **OpenAI** (`OPENAI_API_KEY`) | Learner preference / existing access |
| Qdrant Cloud (vector DB) | **Azure** (deferred) | Introduced when the RAG lectures need it |

---

## 4. The per-episode workflow

### Before coding

**Step 1 — Orient.** Read `COURSE_PROGRESS.md` to confirm where we are. Read the new lecture's `.md` end to end before commenting on it.

**Step 2 — Scaffold.** Create `WeekN/episode-NN-short-title/`:
- `source-notes.md` — the learner's raw lecture notes, preserved **unmodified**
- `notes.md` — from `templates/episode-notes-template.md`
- `assessment.md` — from `templates/episode-assessment-template.md`
- `code/` — only if the episode involves code

**Step 3 — Plan aloud.** State what the episode covers, what will be built, which new Python concepts will appear, and the assessment tier (§5). Confirm before writing code.

### Learning and building

**Step 4 — Teach one concept at a time.** Explain → minimal example → C# comparison → learner implements → review → improve. Only then move on.

**Step 5 — Learner writes the code.** The tutor sets up the file and explains what each part must do. The learner fills in the logic.

### Verification

**Step 6 — Run and verify.** The learner runs the code and pastes **actual output**. Nothing is declared working because it *looks* right. Debugging failures is part of the lesson — and every real error gets logged in `PYTHON_GOTCHAS.md`.

### Assessment

**Step 7 — Run the episode assessment.** See §5. This is mandatory and is what separates "I followed along" from "I understand this."

### Documentation

**Step 8 — Write the notes.** Fill in `notes.md` from the template.

**Step 9 — Update shared references.** `GLOSSARY.md` (new terms + C# analogy), `CHEATSHEET.md` (commands run for the first time), `PYTHON_GOTCHAS.md` (traps hit), `RESOURCES.md` (new links), `WeekN/README.md` (episode index).

**Step 10 — Journal.** The learner's reflection answers from the assessment are carried into `LEARNING_JOURNAL.md` **in their own words**. Anything flagged as shaky goes on the rolling revisit list. Confidence goes into `COURSE_PROGRESS.md`.

### Closing out

**Step 11 — Commit, update progress, push.** Update `COURSE_PROGRESS.md`, propose commits explaining *why*, push.

**Step 12 — Week review.** At the end of each week, before starting the next: run the week review (§8).

---

## 5. The episode assessment

Completing a lecture is not the same as understanding it. The assessment checks whether the learner can **explain, apply, and debug** the material — not whether they can recall it.

### Tiers

Not every episode can carry a full assessment. Forcing four parts onto a pure-setup episode produces filler, and filler is how a process becomes box-ticking that gets skipped. The tier is chosen in step 3 based on what the episode actually contained.

| Tier | When | Parts |
|---|---|---|
| **0** | Setup / conceptual only, no code written | Concept check + reflection |
| **1** | Light code — a few lines, one new idea | Concept check + coding challenge + reflection |
| **2** | Substantial code or multiple new concepts | All four parts |

**Time caps — enforced.** Coding challenge ≤15 minutes. Debugging challenge ≤5 minutes. Small and consistently done beats ambitious and skipped.

### Part 1 — Concept check

A few short questions requiring explanation **in the learner's own words**:
- Why does this exist? What problem does it solve?
- When should it be used — and when shouldn't it?
- How does it compare to the C#/.NET equivalent?

The tutor responds to each answer: what was right, what was imprecise, what was missing. A vague answer gets probed, not accepted.

### Part 2 — Coding challenge

A small exercise using **only concepts from the current and earlier episodes** — never anything not yet taught.

The learner attempts it **before receiving any hint**. The tutor does not volunteer hints, and does not move down the ladder unless the learner has made an attempt or explicitly asks:

| Level | What the tutor gives |
|---|---|
| 1 | A question that redirects thinking |
| 2 | Names the concept involved, points at docs |
| 3 | Structure or pseudocode — no Python |
| 4 | Partial code with the key line missing |
| 5 | Full solution, with a line-by-line explanation |

Hints used are recorded in `assessment.md`. Needing level 4 isn't failure — it's data about what to revisit.

### Part 3 — Debugging challenge

A short broken snippet. The learner must **find the bugs, explain why each is wrong, and fix them**.

Bugs are drawn from `PYTHON_GOTCHAS.md` — real traps that catch C# developers, preferring mistakes the learner has actually made. Synthetic typo-hunting is not the exercise; recognising *characteristic Python failure modes* is.

### Part 4 — Reflection

Asked at the end, and **only after the coding challenge** — confidence rated before attempting to apply something is systematically inflated.

1. Biggest thing you learned?
2. What still feels unclear?
3. What mistakes did you make?
4. Which Python concept felt most alien coming from C#?
5. What do you want to revisit later?
6. Confidence, 1–5? *(1 = lost · 3 = could follow along · 5 = could rebuild from scratch)*

**Calibration is part of the tutor's job.** If a rating contradicts how the assessment actually went — a 5 after needing level-4 hints — the tutor says so and asks the learner to reconsider. A tracker full of inflated ratings points review time at the wrong places, which is worse than having no tracker.

---

## 6. Definition of done

An episode is complete only when **all** of these are true:

- [ ] All code from the lecture written **by the learner** and running correctly
- [ ] Real output pasted, verifying it works
- [ ] Learner can explain what each part does and why
- [ ] **Concept check answered** and reviewed
- [ ] **Coding challenge attempted** *(Tier 1–2)*
- [ ] **Debugging challenge attempted** *(Tier 2)*
- [ ] `notes.md` complete — no placeholder sections
- [ ] `assessment.md` complete
- [ ] `GLOSSARY.md` / `CHEATSHEET.md` / `PYTHON_GOTCHAS.md` / `RESOURCES.md` updated if anything new appeared
- [ ] `LEARNING_JOURNAL.md` entry written in the learner's own words
- [ ] `COURSE_PROGRESS.md` shows status, date, and confidence
- [ ] Committed with a meaningful message and pushed

### The pressure valve

A hard gate with no escape hatch creates a stalled queue: one unfinished exercise blocks the course for weeks and the whole system gets abandoned.

So an episode may be marked **`✅ Complete (follow-ups)`** when the core work is done but an assessment item was deferred. The deferred item **must** go onto the journal's revisit list and **will** be picked up in that week's review. This is a deferral, not a skip.

What may *never* be deferred: working code, verified output, and the journal entry.

---

## 7. Reflection and honesty

The tutor **never invents** assessment answers, journal entries, or confidence ratings. An unanswered section stays blank. A journal full of plausible-sounding fabrications is worse than an empty one, because it looks like a record of learning while containing none.

---

## 8. Week review

Run at the end of each week, before the next begins. Uses `templates/week-review-template.md`, saved as `WeekN/week-N-review.md`.

**Why end-of-week rather than every N episodes:** it lands at roughly five episodes anyway, but aligns with the course's own thematic boundaries instead of an arbitrary count.

**Why it exists:** episodes assessed in isolation stay isolated. Real understanding shows up when concepts have to combine — and spaced repetition catches what quietly faded.

**Structure:**
1. **Targeted review** — driven by the revisit list and any episode rated ≤3. Deliberately *not* an even sample: review time goes where the learner is weak.
2. **Integration exercise** — one small build combining concepts from multiple episodes. A build, not a quiz.
3. **Retention check** — questions from *earlier* weeks, to surface decay.
4. **Where I stand** — what's solid, what's still shaky, what carries forward.

Larger integration exercises that outgrow a `code/` folder graduate to `projects/`.

---

## 9. Conventions

### Naming
- Weeks: `Week1/`, `Week2/`, …
- Episodes: `episode-NN-short-kebab-title/` — zero-padded so they sort correctly
- Projects: `projects/descriptive-name/` — named, not numbered

### `code/` vs `projects/`
- **`code/`** — short practice scripts for exactly one episode. Disposable.
- **`projects/`** — applications spanning multiple episodes, with their own lifecycle.

### Commit messages
`<type>: <what changed>`, with a body explaining *why* when it isn't obvious.

| Type | Used for |
|---|---|
| `feat` | new working code or functionality |
| `docs` | notes, README, glossary, journal, progress, assessments |
| `chore` | tooling, dependencies, config |
| `refactor` | restructuring without behaviour change |
| `fix` | correcting something broken |

A completed episode typically produces one or two commits, e.g.
`feat: episode 04 — first OpenAI chat completion call` then
`docs: episode 04 notes, assessment, and journal entry`.

### Secrets
`.env` is **never** committed. New variables are documented in `.env.example` with dummy values.

---

## 10. Environment

Single `uv` project at the repository root — one `pyproject.toml`, one `.venv`, shared by all weeks and projects.

```bash
uv sync                 # install/refresh dependencies into .venv
uv add <package>        # add a dependency (updates pyproject.toml + uv.lock)
uv run <script.py>      # run a script inside the project's venv
```

**Planned escape hatch:** if a project in `projects/` eventually needs conflicting dependencies, `uv` supports *workspaces* (conceptually a `.sln` containing several `.csproj`). Deliberately not set up yet — unnecessary complexity until a real conflict appears.
