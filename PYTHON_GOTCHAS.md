# Python Gotchas for a C# Developer

Traps that specifically catch developers arriving from C#/.NET.

This file has a **functional role** in the workflow, not just a documentary one: debugging challenges in episode assessments are drawn from here, so the bugs I practice are real traps rather than synthetic ones. Entries marked **[hit]** are mistakes I actually made.

---

## The root cause of most surprises

C# is **statically typed and compiled**. The compiler catches typos, type errors, wrong argument counts, and unreachable code *before* the program runs.

Python is **dynamically typed and interpreted**. Almost nothing is checked until the offending line actually executes. A typo in a rarely-taken branch can survive into production and fail months later.

**Practical consequence:** in C# "it compiles" is weak evidence of correctness. In Python there is no equivalent signal at all — running the code is the only feedback. This is why the workflow insists on running everything and pasting real output.

**Two axes, not one** — a common confusion worth getting straight:

| | Static ↔ dynamic (*when* types are checked) | Strong ↔ weak (*how strictly* enforced) |
|---|---|---|
| **C#** | Static — compile time | Strong |
| **Python** | Dynamic — runtime | **Strong** |
| JavaScript | Dynamic | Weak — `"5" - 2` gives `3` |

**Python is strongly typed.** `"5" - 2` raises `TypeError`; it will not silently coerce. The difference from C# is *when* you find out, not *whether*. "Python lets anything happen" is false; "Python won't tell you until that line runs" is true.

---

## Syntax and structure

### Indentation is load-bearing

```python
if x > 0:
    print("positive")
    print("also runs")   # inside the if
print("always runs")     # outside — indentation alone decides this
```

In C# indentation is cosmetic and braces define scope. In Python indentation *is* the scope. Mixing tabs and spaces, or being off by one level, either raises `IndentationError` or — far worse — silently changes what the code does.

### No braces, no semicolons; a colon opens a block

```python
def greet(name):        # colon, then indented body
    return f"Hi {name}"
```

### Importing a module *executes* it **[hit — Ep 01 assessment Q3]**

There is no separate declaration phase in Python. Importing a file runs it top to bottom; `def` and `class` are statements that *execute* to bring the function or class into existence.

```python
# greeter.py
def main():
    print("Hello!")

main()          # bare call at top level
```

```python
import greeter  # prints "Hello!" — merely importing ran it
```

Guard anything that should only run when the file is the entry point:

```python
if __name__ == "__main__":
    main()
```

**Why it catches a C# developer:** C# has exactly one `Main`, and referencing an assembly executes nothing. In Python every file is both runnable and importable, and its top level is live code. Any top-level statement — a print, an API call, a database connection — fires on import.

### Truthiness — every type can be tested as a bool

```python
if not api_key:        # fires for None AND for ""
```

Falsy values: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`.

Convenient for a key check — it's exactly `string.IsNullOrEmpty(apiKey)`. Dangerous everywhere else:

```python
if not item_count:     # BUG: also fires when item_count is legitimately 0
if not results:        # fires for an empty list — usually intended, sometimes not
```

A C# developer reads `if not x` as a null check. Python also treats zero, empty string, and empty collection as falsy, so a valid `0` silently takes the error branch. When you mean "is it None", write `if x is None:`.

### Dict keys are unchecked strings **[hit — Ep 02]**

```python
{"role": "user", "prompt": "..."}    # typo — Python is perfectly happy
```

A dict key is a runtime string; nothing validates it. Python builds the dict, the SDK serialises it, it crosses the network, and the **server** rejects it. Your feedback arrives as an HTTP error from someone else's machine.

In C#, an SDK exposes a `ChatMessage` class and `msg.Prompt = "..."` is a red squiggle before you save.

### Assigning a name from itself before it exists **[hit — Ep 02 debugging challenge]**

```python
message = {"role": "user", "content": "Say hello"}
messages = [messages]        # NameError — 'messages' doesn't exist yet
```

Valid syntax, so nothing complains until the line runs. In C# this is a compile error you could never ship.

**The wider lesson from where this happened:** it appeared in a *fix* for a bug that had been correctly identified. Finding a bug and fixing it are different skills — attention moves on once the bug is spotted and the correction gets typed on autopilot. Python won't check the correction for you. **Run the fix.**

### `snake_case`, not `PascalCase`

Python convention ([PEP 8](https://peps.python.org/pep-0008/)): functions and variables are `snake_case`, classes are `PascalCase`, constants are `UPPER_SNAKE`. Writing `GetUserName()` in Python looks as wrong to a Python developer as `get_user_name()` looks in C#.

---

## Project and environment

### Forgetting the virtual environment **[hit — conceptually]**

Running `python script.py` uses the *system* Python and will not see packages installed into the project's `.venv`. The error is usually `ModuleNotFoundError` for a package you know you installed.

**Rule for this repo:** always `uv run script.py`, never bare `python script.py`.

### Ignoring the lockfile **[hit]**

The first `.gitignore` draft excluded `uv.lock`. Wrong — `uv.lock` is the equivalent of `packages.lock.json` and must be committed. Ignore `.venv/` (regenerable, like `bin/`/`obj/`); commit `uv.lock`.

---

## Coming soon

Entries are added as concepts are introduced. Deliberately **not** pre-populated with traps from features we haven't covered yet — that would violate the no-skipping-ahead rule.

Known landmines to document when we reach them: mutable default arguments, `is` vs `==`, late-binding closures, shallow vs deep copy, truthiness of empty collections, and integer caching.
