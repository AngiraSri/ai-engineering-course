# Projects

Complete applications that span multiple episodes and have their own lifecycle.

## Why this is separate from episode `code/`

| | `WeekN/episode-NN/code/` | `projects/` |
|---|---|---|
| **Purpose** | Demonstrate one concept from one lecture | Build a real, working application |
| **Lifespan** | Written once, rarely revisited | Grows across many episodes |
| **Scope** | A script | A structured application |
| **Example** | "call the API and print the response" | "a document Q&A system with retrieval and a chat interface" |

Tying a multi-week RAG system to `Week4/episode-22/code/` would bury it — its history would look like it belongs to a single lecture, and it would be unfindable later. Projects get their own home.

---

## Conventions

Each project is a folder named descriptively (not numbered — projects aren't sequential):

```
projects/
└── document-qa/
    ├── README.md      # what it does, how to run it, which episodes fed into it
    └── src/
```

Every project's `README.md` must state:
- what the project does
- how to run it
- which episodes/concepts it draws on
- current status

**Dependencies:** projects currently share the repository's single root `pyproject.toml` and `.venv`. If a project ever needs conflicting dependencies, we'll introduce `uv` workspaces at that point — see [LEARNING_GUIDE.md §8](../LEARNING_GUIDE.md#8-environment).

---

## Index

| Project | Description | Status | Episodes drawn from |
|---|---|---|---|
| — | *No projects yet. The first will appear once the lectures move beyond single-concept scripts.* | | |
