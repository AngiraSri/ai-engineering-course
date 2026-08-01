# Week 1 — Foundations & Setup

## Episodes

| Ep | Title | Status | Notes |
|---|---|---|---|
| 01 | Course Intro + Tech Stack Setup | ✅ Complete | [notes](episode-01-intro-setup/notes.md) |

## Theme

Getting the development environment working and understanding the shape of the course.
No AI code yet — Episode 01 is entirely tooling: Python, `uv`, Git, and API credentials.

## Key takeaways so far

- The Python toolchain (`uv`, venv, `pyproject.toml`) maps closely onto the .NET toolchain, with the venv being the one genuinely new idea.
- Secrets live in `.env`, which is git-ignored from the very first commit — not retrofitted later.
- We use **OpenAI** rather than the course's Groq, and defer the vector database to Azure.
