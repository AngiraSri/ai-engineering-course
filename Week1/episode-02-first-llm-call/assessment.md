# Episode 02 — Assessment

| | |
|---|---|
| **Tier** | 2 — substantial code, several new concepts |
| **Date** | started 2026-08-02, completed 2026-09-14 |
| **Notes** | [notes.md](notes.md) |
| **Code** | [code/](code/) |
| **Result** | Concept check ✅ · Coding challenge ✅ (no hints) · Debugging 5/5 identified, clean fix on 2nd pass |

Answers are written **by me, in my own words**. Blank sections stay blank rather than being filled in by the tutor.

---

## 1. Concept check

**Q1.** The API made you wrap a single message in a list (`[message]`). Why does it work that way instead of just accepting one message?

**My answer:**

     Because we send multiple message to LLM. That is LMM API accepts a list of message. 
**Tutor feedback:** ✅ Correct, but it stops one step short of *why*. "The API accepts a list" restates the observation; the question is what the list is **for**.

Your own Q6 answer has it: the API is **stateless**. The server keeps nothing between calls, so the list isn't a convenience for batching — **the list *is* the conversation**. One message is just a conversation of length one, which is why there's no special-case shape for it.

That reframing matters practically: as a chat grows, that list grows, and you pay for every token in it on every single call. The list is the thing you will eventually have to manage, trim, and summarise.

---

**Q2.** Why is the reply at `response.choices[0].message.content` rather than something like `response.answer`? What would ever put more than one item in `choices`?

**My answer: Becuase LLM can give more than one response a question that is why choices as is array**

 
**Tutor feedback:** ✅ Right. The half you left out is *what actually puts more than one there*: a parameter called `n`. Pass `n=3` and you get three independently generated completions in `choices`, billed for all three.

Why anyone would want that: generating several candidates and picking the best (by a scoring function, or by another model) is a real production technique for improving quality. You're spending tokens to buy a better answer.

Default is `n=1`, which is why `choices` is a one-element list in everything we've written — and why `[0]` is not a magic incantation but a genuine index into a genuine list.

---

**Q3.** `{"role": "user", "prompt": "..."}` is a valid Python dict, so Python runs it happily and the *server* rejects it. Explain why this class of mistake is possible in Python but not in C#. What does that change about how you should test Python code?

**My answer:  This is mainly because Python is dynamically typed, while C# is statically typed.  Python sees this as a perfectly valid dict. Python doesn't automatically know that the server expects something.So Python happily creates the dictionary and sends it. The error may only appear when the API/server validates the request.
For C# if we have strongly typed request model, the compiler catches it before the program runs

So the key difference is:

C# → compiler catches many structural mistakes
Python → runtime/API may catch them

Not sure about the second part of question. 

**


**Tutor feedback:** ✅ The best answer you've written so far. "The compiler catches structural mistakes / runtime or the API catches them" is exactly the distinction, and you reached it unprompted.

**Second half — what it changes about testing.** In C#, the compiler is a free test suite that runs on every build and proves whole categories of error impossible: misspelled members, wrong types, wrong argument counts. Python gives you none of that, so **that work has to be replaced deliberately, not assumed**:

1. **Every line must actually execute to be verified.** A typo inside an `if` branch you never hit is a live bug. C# would have caught it at build; Python finds it in production.
2. **Run in small increments.** This is why we ran the script after sections 1–3 rather than writing all 7 and running once — you shrink the search space for where it broke. That habit matters far more in Python than in C#.
3. **Tests carry weight the compiler used to carry.** In .NET a test suite checks *behaviour*. In Python it also has to check *structure* — that the code even holds together.
4. **Tooling buys some of it back:** type hints + a checker (`mypy`, `pyright`) and a linter (`ruff`) recover a slice of compile-time safety. Optional, not automatic — and the reason serious Python codebases adopt them.

The honest summary: Python trades guaranteed-early feedback for flexibility. You pay that back with discipline.

---

**Q4.** Your call used 14 prompt tokens and 145 completion tokens. If you were trying to cut the cost of a production app making this call a million times a day, where would you look first, and why?

**My answer:** I would also enforce a maximum output length using the API's output-token limit (for example, max_output_tokens, depending on the API/model) 
Also if require I will use system role with a prompt like 
"Answer in one line. Be concise. Do not provide explanations unless explicitly asked."


**Tutor feedback:** ✅ Correct, and you went to the right place first. Output was 10× input and costs ~4× more per token, so **completion length is where the money is**. Both levers you named — a hard `max_tokens` ceiling and a system prompt demanding brevity — are what a real team reaches for.

Worth knowing they behave differently: `max_tokens` **truncates** (a hard cut mid-sentence), while a system prompt **asks** (usually obeyed, never guaranteed). Production code typically uses both — the prompt for quality, the ceiling as a cost circuit-breaker against a model that ignores instructions and rambles.

Three other levers once those are exhausted:
- **A smaller/cheaper model** — most calls don't need the biggest one. Routing easy requests to a cheap model is a standard cost architecture.
- **Prompt caching** — that `cached_tokens=0` field. A long system prompt resent a million times is a lot of repeated input; providers discount prefixes they've already seen.
- **Not calling the model at all** — cache identical requests. The cheapest call is the one you skip.

---

**Q5.** The reply said *"As of my last update in October 2023."* What does that reveal about how the model works, and what specific problems does it create for a real application? Name at least two.

**My answer:** It reveals that the model has a knowledge cutoff. A model's knowledge is not necessarily real-time knowledge.

Outdated information
    If you ask about current product prices, APIs, company policies, news, etc., the model may give an old answer.
Wrong decisions based on stale data
    An application could make a recommendation or business decision using information that is no longer true.


**Tutor feedback:** ✅ Knowledge cutoff identified, two concrete problems named as asked.

One more that's arguably the biggest, and it isn't about *time*: **the model has never seen your private data.** Not your codebase, your customer records, your internal wiki, your contracts. That's not a staleness problem — that information was never in training and never will be, no matter how recent the model.

So there are two distinct gaps, and conflating them will confuse the RAG lectures:

| Gap | Example | Fixed by |
|---|---|---|
| **Temporal** — trained before it happened | "Who won last night?" | Retrieval, or a web-search tool |
| **Private** — never in training at all | "What's in our Q3 contract with Acme?" | Retrieval over *your* documents |

Both are solved the same way — fetch the relevant text and put it in the prompt — which is exactly what Week 3 builds.

And one failure mode worth fearing more than staleness: this model *told you* its cutoff and hedged. **Models don't always do that.** Ask about something just past the cutoff and you can get a fluent, confident, entirely invented answer. Stale-and-honest is a nuisance; confident-and-wrong is the one that reaches production.

---

**Q6.** There are three roles: `system`, `user`, `assistant`. What is each for? And why does a chatbot have to resend the entire conversation on every single call instead of the server remembering it?

**My answer:**

System - Instration to model
User - User's input
Assistant - LLM Response

The API call is generally stateless from the model's perspective.
Model need context to answer
Why is this designed this way?
It gives your application control over the conversation state.

Your application/database can decide:

what history to keep
what history to remove
what information to summarize
what context to add
which conversations belong to which user

So think of it like this:

The model generates the response; your application manages the conversation memory/context.


**Tutor feedback:** ✅ Strongest answer of the set. Roles correct, statelessness correct — and the closing line is a genuine engineering insight, not a restatement:

> *"The model generates the response; your application manages the conversation memory/context."*

That is the correct mental model, and most people take much longer to arrive at it. Everything in Weeks 4–5 about agents and memory is built on exactly that split. Your list of what the application decides — what to keep, drop, summarise, whose conversation is whose — is essentially the job description of the layer you'll be writing.

Two things to add:

**Statelessness is a design choice with consequences you own.** Horizontal scaling is trivial (any server can handle any request, nothing to synchronise), but *you* become responsible for persistence, and a naive implementation resends the entire history every turn. Cost grows **quadratically** with conversation length — turn 50 pays for turns 1–49 again. That's why trimming and summarising are engineering work, not polish.

**One nuance on `system`:** it sets behaviour, but it is not a security boundary. A user message can talk the model out of its system prompt — that's prompt injection, and it's a real vulnerability class you'll meet properly later. Treat `system` as strong guidance, never as enforcement.

---

## 2. Coding challenge

The lecture *explains* roles and conversational context but never codes them. This challenge does — so it completes the episode as well as testing it.

**Task.** Create `code/chat_with_context.py`. Two parts:

**Part A — a system prompt.** Same setup as `hello_llm.py`, but the messages list starts with a `system` message that constrains behaviour. Use something checkable, e.g. *"Answer in exactly one sentence. No greetings, no caveats."* Ask any question and confirm the constraint actually held.

**Part B — prove context works.** Build a messages list representing a conversation that has already happened, then ask a follow-up that is meaningless without it:

1. `user`: "Who is Virat Kohli?"
2. `assistant`: (a short answer you write yourself — you are fabricating history, which is allowed and is exactly how chat apps work)
3. `user`: "What is his age?"

Send all four messages (system + those three) in one call. The reply should resolve *"his"* to Kohli. Then, as a control, send **only** `"What is his age?"` with no history and compare.

**Constraints:** only concepts from Episodes 01–02 — dicts, lists, keyword arguments, `os.getenv`, the client. No new packages, no functions or loops needed.

**Hints used:** none / level 1 / level 2 / level 3 / level 4 / full solution

**What I observed (with vs without history):**

_(not recorded — see review)_

**Tutor review:** ✅ [`chat_with_context.py`](code/chat_with_context.py) is correct. System message first, fabricated assistant turn in the right place, four messages in one call, `[0]` index right, usage printed. No hints used.

**Two things you did that I didn't ask for, both worth commenting on:**

1. **`OpenAI()` with no arguments.** This works — the SDK looks for `OPENAI_API_KEY` in the environment itself, and `load_dotenv()` has already put it there. You noticed the explicit pass-through was redundant and dropped it, along with `import os`. That's real understanding rather than copying, and it's how most production code is written.

   The trade-off: you also dropped the `if not api_key` guard, so a missing key now surfaces as an SDK error rather than your own message. Acceptable here; worth being a deliberate choice rather than a side effect.

2. Consistent formatting on the dicts, which keeps a growing list readable. Python style puts no space before the colon (`"role": "system"`, not `"role" : "system"`) — a formatter would fix it, and it's cosmetic.

⚠️ **But the challenge is incomplete — the part that mattered is missing.** The task was to run it **with** history and then again with **only** `"What is his age?"`, and compare. Building the code was the easy half; the control run is where the concept gets proven. Without it you have a script that works, not an observation.

What to do: comment out the first two messages (or make a second list with just system + the final question), run it, and record both replies. **Predict what the second one will say before you run it.**


First response

Virat Kohli is a highly successful Indian cricketer known for his aggressive batting style and numerous records in international cricket.
CompletionUsage(completion_tokens=25, prompt_tokens=30, total_tokens=55, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=None, cached_tokens=0))

Second response

C:\Users\asrivastava\OneDrive - Guidepoint\Desktop\sprints\Learning\Baisc AI Learning\Week1\episode-02-first-llm-call\code>uv run chat_with_context.py
Virat Kohli was born on November 5, 1988, making him 34 years old as of now.
CompletionUsage(completion_tokens=25, prompt_tokens=72, total_tokens=97, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=None, cached_tokens=0))
 
**Tutor review of the runs:**

✅ **Context is proven.** Run 2 sent the full history (72 prompt tokens) and the model resolved *"his"* → Kohli without being told who "he" was. That's the concept working.

📊 **Notice the token growth:** 30 → 72 prompt tokens for the same system prompt. Nothing was added except conversation history, and the input bill more than doubled. Extend that to a 50-turn chat and you can see why trimming history becomes engineering work rather than polish.

⚠️ **That wasn't the control, though.** Run 1 asked *"How is Virat Kohli?"* on its own — the **first** question without history. The control was meant to be the **ambiguous follow-up** alone: system + *"What is his age?"* and nothing else. That's the run that shows the model with no way to know whose age is being asked. Still worth doing — it takes one edit.

---

### 🔴 The most important thing in this episode is sitting in your run-2 output

> *"Virat Kohli was born on November 5, 1988, making him **34 years old as of now**."*

**He isn't 34. He's 37.** The birthdate is right; the arithmetic is wrong. And 34 isn't a random error — **34 is how old he was around 2022–23**, which is exactly where this model's knowledge stops.

Unpack what the model actually did:

1. Recalled a stable fact correctly — the birthdate.
2. Computed an age against its *internal* sense of "now," which is frozen near its training cutoff.
3. Stated the result as **"as of now"** — with no hedge, no caveat, no "as of my last update."

Compare that to `hello_llm.py`, where it politely announced its cutoff and told you to check the news. **Same model, same session, opposite behaviour.** You cannot rely on it to flag its own staleness.

This is precisely the failure mode from your Q5 feedback — *stale-and-honest is a nuisance; confident-and-wrong is what reaches production* — and you produced a live specimen within the hour. Note the shape of it, because it generalises far beyond dates: anything the model **derives** from a frozen fact inherits the frozen-ness, while sounding exactly as confident as a correct answer.

A test asserting "the model returns Kohli's age" would have passed in 2023 and silently started lying since. That's the category of bug you'll spend real time on later — and it's the concrete reason Week 3 exists: for anything time-sensitive or private, you supply the facts rather than trusting recall.

Logged in [PYTHON_GOTCHAS.md](../../PYTHON_GOTCHAS.md)? No — this isn't a Python trap. It's in [GLOSSARY.md](../../GLOSSARY.md) under *knowledge cutoff*, because it's a property of the tool itself.

---

## 3. Debugging challenge

Five bugs. Four are things that are *there and wrong*; one is something **missing**. Find all five, say why each is wrong, and fix them. Don't run it first — read it.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=api_key)

messages = {"role": "user", "content": "Say hello"}

response = client.chat.completions.create(
    model="gpt-4o-mini",
    message=messages
)

print(response.choices.message.content)
```

**Bugs I found:**

| # | Problem                          | Fix                    |
| - | -------------------------------- | ---------------------- |
| 1 | Wrong/mismatched API-key env var | `OPENAI_API_KEY`       |
| 2 | `messages` is a dict             | Make it a list         |
| 3 | `message=`                       | `messages=`            |
| 4 | `choices.message`                | `choices[0].message`   |
| 5 | No API-key validation            | Check `if not api_key` |

**Bugs I missed:**

**Fixed code:**

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Please set it in your .env file.")

client = OpenAI(api_key=api_key)

message = {"role": "user", "content": "Say hello"}
messages = [message]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)

```python

```

**Tutor feedback — identification: 5/5. ✅**

All four commission bugs, **and the omission**. In Episode 01 the missing `.venv/` in a `.gitignore` walked straight past you; this time you caught the missing validation. That was the specific weakness on your revisit list, and it's closed. Worth noting properly.

⚠️ **But the fixed code doesn't run.** Three defects — and this is the more interesting result, so it's worth being precise:

| | Your fix | Problem |
|---|---|---|
| 1 | `os.getenv("OPEN_AI_KEY")` | Still wrong. Your table said `OPENAI_API_KEY` — correct — but the fix says `OPEN_AI_KEY`. A *different* wrong name. Same bug, new spelling |
| 2 | `messages = [messages]` | **`NameError` — crashes on this line.** You renamed the dict to `message` but wrapped `messages`, which doesn't exist yet. Self-referential |
| 3 | *(missing)* | The `if not api_key` check you identified as bug #5 **never made it into the fix** |

**The lesson — finding a bug and fixing it are different skills.** You scored full marks on the first and stumbled on the second, which is more common than it sounds: attention moves on once the bug is *spotted*, and the fix gets typed on autopilot. This is exactly why "I've fixed it" is not a claim anyone should accept without a run — in Python especially, where nothing checks your work until execution.

Defect 2 is the one to sit with: in C#, `messages = [messages]` before `messages` exists is a compile error — you'd never see it run. In Python it's a perfectly valid line that fails at runtime. That's Q3's answer biting in practice, ten lines after you wrote it.

And notice defect 3: **you identified an omission, then omitted the fix for it.** The pattern is narrowing but hasn't disappeared — it's moved from *spotting* to *finishing*.

**Redo the fixed code, then actually run it.** All three defects are visible on a careful read; the run is what proves it.

---

**Tutor feedback on the redo: ✅ all three defects fixed, code is correct.**

`OPENAI_API_KEY` spelled right · the `if not api_key` guard is in · `messages = [message]` wraps the right name · `messages=` keyword · `choices[0]`.

Final score: **5/5 identification, clean fix on the second pass.**

One nit, and it's the same nit as everywhere else in this episode: **no output pasted, so the redo is unverified.** The code reads correctly to me and I'd expect it to run — but "reads correctly" is the claim the first version also had. You've now got direct evidence of how that goes.

**Biggest thing I learned:** LLM API response is stateless. We just send instructions. But the whole conversation  is controlled by application. How much context or memory LLM server in next message will receive is decided by application. 

**Still unclear:** : More new concepts

**Mistakes I made:**  :  

**Most alien Python concept vs C#:** Python is dynamically typed and C# is strongly typed.

**To revisit later:**

**Confidence (1–5):**
> Rated *after* the coding challenge, not before.
> 1 = lost · 2 = shaky · 3 = could follow along · 4 = solid · 5 = could rebuild from scratch

Rating - 4

**Tutor feedback on the reflection:**

**One precision worth fixing, because you've now written it twice:** *"Python is dynamically typed and C# is strongly typed"* mixes two independent axes.

|  | Static vs dynamic (*when* types are checked) | Strong vs weak (*how strictly* types are enforced) |
|---|---|---|
| **C#** | Static — at compile time | Strong |
| **Python** | Dynamic — at runtime | **Strong** |
| JavaScript | Dynamic | Weak — `"5" - 2` gives `3` |

**Python is strongly typed.** `"5" - 2` raises `TypeError`; it will not silently coerce. What differs from C# is *when* — runtime, not compile time.

This isn't pedantry: it's the difference between "Python will let anything happen" (false) and "Python won't tell you until that line runs" (true). Your `messages = [messages]` bug is the second thing, not the first — the language caught it, just later than C# would have.

**Confidence 4 — accepted, and I think earned this time.** For contrast, I pushed back on your Ep 01 rating of 4; here the evidence supports it. You wrote working code with no hints, found 5/5 bugs including the omission that beat you last time, improved on the spec unprompted (`OpenAI()` reading the env var itself), and Q3/Q4/Q6 were genuinely strong. Calibration has to cut both ways or the number is worthless.

⚠️ **But three reflection fields are empty or vague, and one of them matters.** *"Mistakes I made"* is blank — in the episode whose single most instructive moment was a mistake. You identified five bugs correctly and then shipped a fix with three new ones. That's the thing future-you will benefit from reading, far more than any concept note here. Leaving it blank throws away the most valuable data this episode produced.

*"Still unclear: more new concepts"* isn't really an answer either, and *"To revisit later"* is empty — while your own output contains a model confidently asserting a wrong age.

---

## Completion checklist

- [x] Concept check answered — and reviewed
- [x] Coding challenge attempted — no hints; control run deferred
- [x] Debugging challenge attempted — 5/5 identified, clean on second pass
- [x] `notes.md` complete
- [x] `LEARNING_JOURNAL.md` updated
- [x] `GLOSSARY.md` / `PYTHON_GOTCHAS.md` updated
- [x] `COURSE_PROGRESS.md` updated with status + confidence
- [x] Committed and pushed

**Deferred items:** *(carried to the [revisit list](../../LEARNING_JOURNAL.md#revisit-list) and the Week 1 review)*

1. **The no-history control run** — send system + *"What is his age?"* alone and compare. One edit; the run that shows the model with no way to resolve "his".
2. **Verifying the corrected debug snippet** — the redo reads correctly but was never executed.
3. **Reflection fields left blank** — *Mistakes I made* and *To revisit later*.
