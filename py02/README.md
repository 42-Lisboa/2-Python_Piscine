# 🛡️ py02 — Garden Guardian

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Data Engineering for Smart Agriculture. Builds on py00 and py01 to create resilient data pipelines using Python's exception handling system: try/except/finally, raising exceptions, custom error types, and fault-tolerant design.

---

## 📋 Summary

- [Exercises](#exercises)
- [Key Techniques](#key-techniques)
- [General Rules](#general-rules)
- [Concepts Learned](#concepts-learned)
- [Resources](#resources)

---

<a name="exercises"></a>
<details open><summary><h2>📂 Exercises</h2></summary>

| # | File | Description |
|---|------|-------------|
| 00 | `ft_first_exception.py` | First `try/except` — catch invalid sensor input |
| 01 | `ft_raise_exception.py` | `raise` — validate temperature range and re-raise on bad data |
| 02 | `ft_different_errors.py` | Multiple exception types — `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError` |
| 03 | `ft_custom_errors.py` | Custom exceptions — `GardenError`, `PlantError`, `WaterError` |
| 04 | `ft_finally_block.py` | `finally` — resource cleanup always runs, even on error |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`try/except`** — catch and handle runtime errors without crashing (ex00)
- **`raise`** — manually trigger exceptions when data is invalid (ex01)
- **Multiple `except` blocks** — catch different error types separately or together (ex02)
- **Built-in exceptions** — `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError` (ex02)
- **Custom exception classes** — inherit from `Exception` or a parent error class (ex03)
- **Exception hierarchy** — catching a parent class catches all its subclasses (ex03)
- **`finally`** — block that always runs for guaranteed resource cleanup (ex04)
- **`try/except/finally`** — full error-handling structure for fault-tolerant pipelines (ex04)
- **Type hints** — all functions annotated with `mypy`-compatible types
- **`flake8`** — PEP8 linting enforced throughout the module

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All functions and methods must include **type hints** — checked with `mypy`
- Each exercise in its own file and directory (`ex0/` through `ex4/`)
- Programs must **never crash** — all errors must be handled gracefully
- Show both **normal operations** and **error scenarios** in each exercise
- Use built-in exception types appropriately; create custom ones when built-ins aren't specific enough

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- Why robust systems are designed to **handle failures gracefully**, not avoid them
- The difference between **catching** an exception and **raising** one
- How Python's **exception hierarchy** allows catching groups of related errors
- When to use **built-in exceptions** vs. creating **custom exception classes**
- How `finally` ensures **resource cleanup** (closing files, connections, systems) always occurs
- How to build **fault-tolerant data pipelines** that keep running when sensor data is corrupt or missing

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="resources"></a>
<details open><summary><h2>🔗 Resources</h2></summary>

| Title | Author | Description |
|-------|--------|-------------|
| [Learn Python EXCEPTION HANDLING in 5 minutes! 🚦](https://youtu.be/V_NXT2-QIlE?si=kPMMjB8teNACWI7x) | [Bro Code](https://www.youtube.com/@BroCodez) | A concise introduction to Python exception handling, covering `try/except`, `finally`, and `raise` with practical examples. |
| [Errors and Exceptions — Python 3 Docs](https://docs.python.org/pt-br/3/tutorial/errors.html) | [Python.org](https://docs.python.org) | Official Python 3 tutorial on error handling: syntax errors, exceptions, `try/except/else/finally`, and defining custom exception classes. |
| [Errors and Exceptions — Python 3.6 Docs](https://docs.python.org/pt-br/3.6/tutorial/errors.html) | [Python.org](https://docs.python.org) | Python 3.6 version of the official errors and exceptions tutorial, useful for understanding the foundations of the exception system. |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>
