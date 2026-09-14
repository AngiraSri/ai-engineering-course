# Learning Journal

My personal record of this course — written in my own words, not a technical reference.

- For **what an episode covered**, see that episode's `notes.md`.
- For **what I want to review**, see the revisit list below.
- This file is chronological. Newest entries go at the bottom, so it reads as a story from episode 1 onward.

---

## Revisit list

Rolling list of things I flagged as shaky. Struck through once genuinely revisited.
Kept here rather than scattered across entries — otherwise these get written down and never acted on.

*From Ep 01 — flagged by the assessment rather than self-identified:*

- [ ] **Importing a Python file executes it** — the `if __name__ == "__main__":` guard, and why top-level code is live on import. *(Ep 01 Q3 — hadn't encountered this. In [PYTHON_GOTCHAS.md](PYTHON_GOTCHAS.md); will return as a debugging challenge.)*
- [x] ~~**`pyproject.toml` vs `uv.lock`** — manifest vs lockfile.~~ *(Ep 01 Q2 → resolved in Ep 02: `uv add openai python-dotenv` installed **18** packages for the 2 requested. `pyproject.toml` records the 2 as a range; `uv.lock` pins all 18 exactly. Demonstrated, not just explained.)*
- [ ] **Truthiness** — `if not x` fires for `None`, `""`, `0`, `[]`, `{}`. Fine for the API-key check; a bug waiting to happen for anything numeric. *(Ep 02)*
- [ ] **Finishing a fix, not just spotting the bug.** Ep 02: found 5/5 bugs, then shipped a fix containing 3 new ones — including omitting the very validation just identified as missing. *(The Ep 01 "errors of omission" pattern, moved from spotting to finishing.)*
- [ ] **Hosted vs local model trade-offs** — cost per call, data privacy, network dependency, version drift. *(Ep 01 Q4 — will matter directly at the Week 8 deployment lectures.)*
- [ ] **Habit, not content: answer every part of a multi-part question.** Three misses in Ep 01 were completeness, not comprehension. *(Applies to code review generally — errors of omission are harder to spot than errors of commission.)*

---

## Entries

### Episode 01 — Course Intro + Tech Stack Setup
**Date:** 2026-08-02 · **Confidence:** 4 · **Assessment:** [Tier 0](Week1/episode-01-intro-setup/assessment.md)

**Most useful thing I learned:**
> Setting up python project and playing around with it.

**Hardest to grasp / still shaky on:**
> All good for now

**Mistakes I made or things that surprised me:**
> Not writing assessment answer fully

**Most alien Python concept coming from C#:**
> No braces

**Tutor note on this entry:**
The self-assessment says "all good," but the concept check found gaps in four of five questions — most notably that importing a Python file *executes* it, which hadn't been encountered at all. The gaps were **completeness, not comprehension**: three questions had two halves and only one half was answered each time. The "mistakes" answer above identifies exactly this, which is the most useful line in the entry.

Confidence recorded as the stated **4**, with a documented split: **4 on the mechanical material** (could rebuild the project setup unaided) and **3 on the conceptual material**. The four items on the revisit list came from this assessment rather than from self-identification — worth noticing, since it's the reason the assessment step exists.

---

### Episode 02 — Understand Your First LLM Call
**Date:** 2026-09-14 · **Confidence:** 4 · **Assessment:** [Tier 2](Week1/episode-02-first-llm-call/assessment.md)

**Most useful thing I learned:**
> LLM API response is stateless. We just send instructions. But the whole conversation is controlled by application. How much context or memory LLM server in next message will receive is decided by application.

**Hardest to grasp / still shaky on:**
> More new concepts

**Mistakes I made:**
_(left blank — see note)_

**Most alien Python concept coming from C#:**
> Python is dynamically typed and C# is strongly typed.

**Tutor note on this entry:**
Clear step up from Episode 01. Concept check was genuinely strong — the closing line of Q6 (*"the model generates the response; your application manages the conversation memory"*) is a real engineering insight and the foundation of the Week 4–5 agent material. Coding challenge written with no hints, plus an unprompted improvement: dropping the explicit `api_key=` after noticing the SDK reads the env var itself. Debugging challenge scored 5/5 on identification **including the error of omission** that was the outstanding Ep 01 weakness — that item is now closed.

Confidence **4 accepted**, unlike Ep 01 where the same rating was challenged. The evidence supports it here.

Two things this entry doesn't record, both worth having:
1. **"Mistakes I made" is blank**, in the episode whose most instructive moment was a mistake — 5/5 bugs found, then a fix shipped containing 3 new ones, including dropping the validation just identified as missing. The second pass was clean. *Finding a bug and fixing it are different skills* is the durable lesson here.
2. **The model returned a confidently wrong answer** and it went unremarked. Asked Kohli's age with correct context, it recalled his birthdate right, computed against its own frozen "now," and said *"34 years old as of now"* — wrong by three years, no hedge, from the same model that had volunteered its cutoff an hour earlier. That single line is the most valuable artefact of the episode and the concrete motivation for everything in Week 3.

**Note on the gap:** roughly six weeks passed between starting and finishing this episode. Worth a quick re-read of `notes.md` before Episode 03, since the Ep 01→02 momentum has cooled.

---
