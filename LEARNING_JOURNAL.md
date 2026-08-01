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
- [ ] **`pyproject.toml` vs `uv.lock`** — manifest (which packages) vs lockfile (which exact versions, incl. transitive). *(Ep 01 Q2)*
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
