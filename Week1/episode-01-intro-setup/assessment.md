# Episode 01 — Assessment

| | |
|---|---|
| **Tier** | 0 — setup/conceptual only, no code written |
| **Date** | 2026-08-02 |
| **Notes** | [notes.md](notes.md) |

Tier 0: concept check and reflection only. No coding or debugging challenge — the episode produced no code of its own, and inventing an exercise here would be filler.

Answers are written **by me, in my own words**. Blank sections stay blank rather than being filled in by the tutor.

---

## 1. Concept check

**Q1.** Why do Python virtual environments exist? What specific problem do they solve that NuGet already solves for .NET?

**My answer:** : Pythion VE exists so that one project dependency don't overlap with other. Its a isolated direclty for each project holding all the dependency for that project specific. 
Comparing it wiht Nuget, nuget install the packages in project whereas Python does it globally by default.
So venv exist to prevent version conflicts between projects.w


**Tutor feedback:** ✅ Correct. Isolation, and the reason it's needed — Python installs globally by default while .NET scopes per project.

One precision worth having: NuGet packages are *physically* stored in one shared global folder (`~/.nuget/packages`), but each project **references** the specific versions it needs, so two projects can reference different versions of the same package without conflict. The isolation is at the *reference* level. Python (pre-venv) had no reference layer at all — `import requests` just finds whatever single copy is installed, so two projects needing different versions genuinely cannot coexist. The venv restores the per-project boundary that .NET has built in.

---

**Q2.** We commit `uv.lock` but git-ignore `.venv/`. Explain the reasoning behind each decision. What would go wrong if we did the opposite?

**My answer:** : Reasoning behind commiting uv.lock is that uv.lock file contains all the dependencies required by the project so we commit it so that when any clone the repo they know all the required dependency and uv will install those packages. 

.venv - it gets created upon running the project so it not required to commit. Similar to how we don't commit bin or obj file in C# project.

If we miss uv.lock, we don't know the dependecny  and generating same env will not possible.

**Tutor feedback:** ✅ The `.venv` half is exactly right, including the `bin`/`obj` analogy.

⚠️ One imprecision on `uv.lock`. It is **not** the file that tells you *which* dependencies the project needs — that's `pyproject.toml`. The split matters:

| File | Says | .NET |
|---|---|---|
| `pyproject.toml` | "this project needs `openai`" | `.csproj` `<PackageReference>` |
| `uv.lock` | "specifically `openai` 1.40.2, which itself pulls `httpx` 0.27.0, which pulls…" | `packages.lock.json` |

So without `uv.lock` you *would* still know the dependencies — you'd just get whatever versions resolve **today**, including transitive ones you never chose. Clone the repo six months apart and you get two different environments from identical source. That's the actual failure, and it's the classic "works on my machine."

⚠️ The second half of the question — *what if we did the opposite and committed `.venv/`* — wasn't answered. Concretely: `.venv` contains absolute paths baked into its config plus platform-specific compiled binaries. Committed and cloned onto another machine (or another OS) it doesn't merely bloat the repo with thousands of files — **it doesn't work at all**. It's not portable by design.

---

**Q3.** What does `if __name__ == "__main__":` actually do, and what would break if we removed it from a file that another file imports?

**My answer:** : if __name__ == "__main__ means run the file only when directly call not as import from other file.
I'm not sure of second question.


**Tutor feedback:** ✅ First half correct. Saying "not sure" on the second half is the right call — here's the answer.

The key thing C# doesn't prepare you for: **in Python, importing a file executes it, top to bottom.** There's no separate "declaration" phase. `def` and `class` statements *run* — that's how the function comes into existence.

So given `greeter.py`:

```python
def main():
    print("Hello!")

main()          # no guard — bare call at top level
```

Then in another file:

```python
import greeter                  # prints "Hello!" — just from importing
print("about to start")
```

You imported the module to reuse `main()`, and importing it *ran* it. The guard prevents exactly this:

```python
if __name__ == "__main__":
    main()                       # only when run directly
```

`__name__` is set to `"__main__"` for the file you launched, and to the module's own name (`"greeter"`) for anything imported. The guard reads: "only run this if I'm the program, not the library."

**Why it bites a C# developer:** in C# there is exactly one `Main` and referencing an assembly never executes anything. In Python every file is both runnable *and* importable, and the top level is live code. Added to [PYTHON_GOTCHAS.md](../../PYTHON_GOTCHAS.md).

---

**Q4.** The course runs models locally with Ollama; we call a hosted API instead. What do we give up with that choice, and what do we gain?

**My answer:** : Local LLM required higher end configuration in system which everyone don't have. Cloud LLM don't need any setup and easy to use. 


**Tutor feedback:** ✅ The *gain* side is right — no GPU, no setup.

⚠️ But the question was two-sided and the **give up** half is largely missing. This matters more than it looks: these trade-offs drive real architecture decisions later in the course, and they're standard AI-engineer interview material.

What a hosted API costs you:

| Give up | Why it matters |
|---|---|
| **Money per call** | Local inference is free after hardware. Hosted bills per token — a retry loop or runaway agent has a literal dollar cost |
| **Data privacy** | Every prompt leaves your machine and goes to a third party. This alone rules out hosted APIs for a lot of enterprise/regulated work |
| **Network dependency** | No internet, no app. Plus latency on every single call |
| **Rate limits** | Throughput is capped by someone else's quota, not your hardware |
| **Version stability** | The provider can deprecate or silently update a model. Your prompts can degrade without you changing a line of code |
| **Vendor lock-in** | Provider-specific APIs and behaviours |

Worth internalising the framing: this is the same **buy vs. build / SaaS vs. self-host** decision you've made before in .NET — the axes (cost, control, privacy, ops burden) are identical. What's *new* in the AI case is version instability: an Azure SQL instance doesn't quietly start returning different answers next month.

---

**Q5.** Spot the problem — this `.gitignore` was proposed for the repo:

```gitignore
.env
__pycache__/
uv.lock
```

What's wrong with it, and why does it matter?

**My answer:** : uv.lock is added in gitignore. Will not awared about the depencdency and may install different version.


**Tutor feedback:** ✅ You found the bug I planted — `uv.lock` must not be ignored. "May install different version" is exactly the consequence.

⚠️ **You missed a second one, and it's arguably worse: `.venv/` is not in the list.** Nothing there excludes it.

The moment you run `uv run main.py`, the venv is created and git sees several thousand untracked files — an entire Python interpreter and every installed package. A careless `git add -A` commits all of it: a repo bloated to hundreds of MB, containing binaries that won't work on anyone else's machine anyway. And once it's in history, removing it later requires rewriting history.

**The transferable lesson:** reviewing a `.gitignore` means checking two things, and the second is the one people skip —
1. Is anything listed that **shouldn't** be? (you caught this — `uv.lock`)
2. Is anything **missing** that should be there? (this one — `.venv/`)

Errors of omission are harder to spot than errors of commission, because there's nothing on screen to look at. Same reason a missing `null` check is harder to see in review than a wrong one. Worth carrying into code review generally.

*(For reference, this was the actual bug sequence in this repo: the first draft correctly ignored `.venv/` but wrongly ignored `uv.lock`. The version in this question is a different, worse variant.)*

---

## 2. Coding challenge

*Not applicable — Tier 0.*

## 3. Debugging challenge

*Not applicable — Tier 0.*

---

## 4. Reflection

**Biggest thing I learned:** : setting up python project and playing around with it.

**Still unclear:**  : All good for now

**Mistakes I made:** : Not writing assessment answer fully

**Most alien Python concept vs C#:** no braces 

**To revisit later:** : Not sure you tell

> **Tutor-suggested** (derived from the assessment, not the learner's own words):
> 1. **Import executes the module** — the `__main__` guard and why top-level code is live. Not previously encountered; logged in [PYTHON_GOTCHAS.md](../../PYTHON_GOTCHAS.md) and will return as a debugging challenge.
> 2. **`pyproject.toml` vs `uv.lock`** — manifest (which packages) vs lockfile (which exact versions, including transitive).
> 3. **Hosted vs local trade-offs** — cost per call, data privacy, version drift. Will matter directly at the deployment lectures in Week 8.
> 4. **Reading habit, not content:** answer *every* part of a multi-part question. Three misses here were completeness, not comprehension.

**Confidence (1–5):**
> 1 = lost · 2 = shaky · 3 = could follow along · 4 = solid · 5 = could rebuild from scratch : 4

> **Tutor calibration note:** recorded as the learner's **4**, with a documented split — **4 on the mechanical material** (could rebuild the project setup unaided) and **3 on the conceptual material** (four of five questions had gaps). Tracked as 4 in `COURSE_PROGRESS.md` with this caveat, so the concept gaps still surface in the Week 1 review.

---

## Completion checklist

- [x] Concept check answered — and reviewed
- [x] Coding challenge — n/a (Tier 0)
- [x] Debugging challenge — n/a (Tier 0)
- [x] `notes.md` complete
- [x] `LEARNING_JOURNAL.md` updated
- [x] `GLOSSARY.md` / `CHEATSHEET.md` / `PYTHON_GOTCHAS.md` updated
- [x] `COURSE_PROGRESS.md` updated with status + confidence
- [x] Committed and pushed

**Deferred items:** none
