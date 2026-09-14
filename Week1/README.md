# Week 1 — Foundations & Setup

## Episodes

| Ep | Title | Status | Notes | Assessment |
|---|---|---|---|---|
| 01 | Course Intro + Tech Stack Setup | ✅ Complete | [notes](episode-01-intro-setup/notes.md) | Tier 0 |
| 02 | Understand Your First LLM Call | ✅ Complete | [notes](episode-02-first-llm-call/notes.md) | Tier 2 |

## Theme

Environment, then the first real API call. Episode 01 is entirely tooling; Episode 02 makes an LLM actually answer something and explains every part of how.

## Key takeaways so far

- The Python toolchain (`uv`, venv, `pyproject.toml`) maps closely onto the .NET toolchain, with the venv being the one genuinely new idea.
- Secrets live in `.env`, git-ignored from the very first commit — not retrofitted later.
- **An LLM call has four parts:** key, client, model, messages. Everything later in the course is orchestration around that call.
- **The API is stateless.** The messages list *is* the conversation, so the application — not the provider — owns memory.
- **Tokens are the unit of cost, and output is the expensive side.**
- **The model does not reliably know what it doesn't know.** Episode 02 caught it confidently returning a three-year-stale age with no hedge — the concrete reason RAG exists.
- We use **OpenAI** rather than the course's Groq, and defer the vector database to Azure.
