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

### LLM (Large Language Model)
A model trained to predict and generate text, accessed here through a hosted API rather than run locally.

### Inference
Running an already-trained model to get an output from an input — as opposed to training it. Every API call we make is one inference.

---

### Token
The unit an LLM reads and writes in — roughly 4 characters, or part of a word. Text is split into tokens before the model sees it, and billing is per token.

**Why it matters:** it's the unit of cost *and* the unit of limits. Two practical surprises:
- Message structure costs tokens too. "How is Virat Kohli?" (5 words) billed 14 prompt tokens — the rest is the chat format's role markers.
- **Output is the expensive side.** Completions typically cost ~4× input per token, and replies are usually far longer than prompts. The main lever on an LLM bill is constraining how much the model *says*.

### Prompt tokens vs completion tokens
`usage` splits every call in two: `prompt_tokens` (what you sent, including all conversation history) and `completion_tokens` (what came back). Priced differently — see above.

### Knowledge cutoff
The date after which a model has seen no training data. Everything it "knows" is frozen there.

**Why it matters — and this is the trap:** a model may *volunteer* its cutoff ("as of my last update in October 2023"), or may not. Observed in Episode 02: asked Virat Kohli's age, the model recalled his birthdate correctly, computed his age against its own frozen sense of "now," and returned **34 as of now** — wrong by three years, stated with no hedge whatsoever.

Anything the model **derives** from a fact inherits the staleness while sounding exactly as confident as a correct answer. Two separate gaps follow from this:

| Gap | Example | Fix |
|---|---|---|
| **Temporal** — happened after training | "Who won last night?" | Retrieval / web search |
| **Private** — never in training at all | "What's in our contract with Acme?" | Retrieval over your own documents |

Both motivate RAG (Week 3).

### Chat Completions vs Responses API
Two OpenAI interfaces for the same underlying models. **Chat Completions** (`client.chat.completions.create`) is what this course uses; **Responses** (`client.responses.create`) is OpenAI's newer, primary-for-new-work API. Both are present in SDK 2.x and Chat Completions is not deprecated.

| | Chat Completions | Responses |
|---|---|---|
| Input | `messages=[{"role","content"}]` | `input=` (string or list) |
| System prompt | a `system` message | `instructions=` |
| Read reply | `response.choices[0].message.content` | `response.output_text` |
| Built-in tools | none | web search, file search, code interpreter |
| State | none — resend history | optional server-side (`previous_response_id`) |

**Why we stay on Chat Completions:** it is the de facto cross-provider standard (Groq, Mistral, vLLM, Ollama and others speak the same shape), so it buys portability. Responses is OpenAI-only. Full reasoning in [LEARNING_GUIDE.md §3](LEARNING_GUIDE.md#3-deviations-from-the-source-course).

### Statelessness
The API remembers nothing between calls. The server holds no session; each request is independent.

**Not a universal law.** This is a *design choice of Chat Completions*. The Responses API can keep conversation state server-side via `previous_response_id`. The trade-off is what actually matters: either the application owns memory (control over what's kept, trimmed and summarised, plus portability) or the provider does (less code, more lock-in). It is a decision, not a constraint.

**Consequence:** the messages list *is* the conversation. To continue one, you resend the whole history every time — so the application, not the provider, owns memory: what to keep, drop, summarise, and whose conversation is whose.

**Cost consequence:** naive implementations grow quadratically — turn 50 pays to resend turns 1–49. Trimming and summarising history is engineering work, not polish.

### Roles (`system`, `user`, `assistant`)
Every message carries a role, which is how the model reconstructs who said what.

| Role | For |
|---|---|
| `system` | Standing instructions that shape behaviour for the whole conversation |
| `user` | What the human/application asks |
| `assistant` | What the model previously replied — including history you fabricate yourself |

**Caution:** `system` is strong guidance, **not a security boundary**. A user message can talk a model out of its system prompt (*prompt injection*). Never treat it as enforcement.

### `choices` and the `n` parameter
Responses arrive as a *list* of completions, not a single answer — hence `response.choices[0].message.content`. The `n` parameter controls how many independent completions to generate (default 1, billed for each). Generating several and picking the best is a real quality technique.

### Client (SDK)
The object holding credentials and connection config, through which calls are made (`client = OpenAI(api_key=...)`).

**C#/.NET analogy:** an `HttpClient` wrapper or a typed service client. Constructed once, reused for many calls.

**Note:** the OpenAI SDK reads `OPENAI_API_KEY` from the environment automatically, so `OpenAI()` with no arguments works once `load_dotenv()` has run.

### RAG (Retrieval-Augmented Generation)
An architecture where relevant documents are retrieved and supplied to an LLM as context, so it can answer questions about data it was never trained on. *(not yet covered in depth — Week 3)*

### Vector database
A database that stores text as numerical vectors and retrieves entries by semantic similarity rather than exact keyword match. The course uses Qdrant; **we are using Azure instead.** *(not yet covered in depth)*

### AI agent
An LLM given tools and a goal, which decides for itself which actions to take in sequence. *(not yet covered in depth — Week 4)*

### MCP (Model Context Protocol)
A standard protocol for exposing tools and data sources to an LLM. *(not yet covered in depth — Week 6)*
