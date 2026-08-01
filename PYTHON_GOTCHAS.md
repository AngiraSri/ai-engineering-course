# Python Gotchas for a C# Developer

Traps that specifically catch developers arriving from C#/.NET.

This file has a **functional role** in the workflow, not just a documentary one: debugging challenges in episode assessments are drawn from here, so the bugs I practice are real traps rather than synthetic ones. Entries marked **[hit]** are mistakes I actually made.

---

## The root cause of most surprises

C# is **statically typed and compiled**. The compiler catches typos, type errors, wrong argument counts, and unreachable code *before* the program runs.

Python is **dynamically typed and interpreted**. Almost nothing is checked until the offending line actually executes. A typo in a rarely-taken branch can survive into production and fail months later.

**Practical consequence:** in C# "it compiles" is weak evidence of correctness. In Python there is no equivalent signal at all — running the code is the only feedback. This is why the workflow insists on running everything and pasting real output.

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
