# 🌿 py01 — Code Cultivation

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Grade-100%2F100-brightgreen?style=for-the-badge" />
</p>

> Object-Oriented Python module from the Piscine. Builds on py00 fundamentals to create a complete digital garden ecosystem using OOP: classes, inheritance, encapsulation, and advanced patterns.

---

## 📋 Summary

- [Exercises](#exercises)
- [Key Techniques](#key-techniques)
- [General Rules](#general-rules)
- [Concepts Learned](#concepts-learned)

---

<a name="exercises"></a>
<details open><summary><h2>📂 Exercises</h2></summary>

| # | File | Description |
|---|------|-------------|
| 00 | `ft_garden_intro.py` | Program entry point with `__name__ == "__main__"` pattern |
| 01 | `ft_garden_data.py` | `Plant` class with attributes and `show()` method |
| 02 | `ft_plant_growth.py` | `grow()` and `age()` methods — simulate a week of growth |
| 03 | `ft_plant_factory.py` | `__init__()` constructor — create plants with initial values |
| 04 | `ft_garden_security.py` | Encapsulation — getters, setters, and input validation |
| 05 | `ft_plant_types.py` | Inheritance — `Flower`, `Tree`, and `Vegetable` subclasses |
| 06 | `ft_garden_analytics.py` | Static/class methods, nested classes, and `Seed` subclass |

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="key-techniques"></a>
<details open><summary><h2>🛠 Key Techniques</h2></summary>

- **`if __name__ == "__main__"`** — program entry point and import safety (ex00)
- **Classes** — `class`, `__init__()`, attributes, and methods (ex01)
- **Instance methods** — `grow()`, `age()`, `show()` operating on object state (ex02)
- **Constructors** — initializing objects with values at creation time (ex03)
- **Encapsulation** — protected attributes (`_attr`), `get_*()`/`set_*()` with validation (ex04)
- **Inheritance** — `Flower`, `Tree`, `Vegetable` extending `Plant`; method overriding (ex05)
- **`super()`** — calling parent class methods from child classes (ex05)
- **Static methods** — `@staticmethod`, logic that doesn't depend on instance state (ex06)
- **Class methods** — `@classmethod`, alternative constructors (ex06)
- **Nested classes** — internal `Stats` tracker class inside `Plant` (ex06)
- **Type hints** — all functions and methods annotated with `mypy`-compatible types
- **`flake8`** — PEP8 linting enforced throughout the module

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="general-rules"></a>
<details open><summary><h2>📐 General Rules</h2></summary>

- Python **3.10+** required
- Code must pass **`flake8`** linter standards
- All functions and methods must include **type hints** — checked with `mypy`
- Each exercise in its own file and directory (`ex0/` through `ex6/`)
- Naming conventions: classes in `PascalCase`, functions and variables in `snake_case`
- Each exercise builds on the previous — the `Plant` class evolves across all exercises

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<a name="concepts-learned"></a>
<details open><summary><h2>📚 Concepts Learned</h2></summary>

- How Python programs are structured and executed (`__main__` entry point)
- Modeling real-world entities with **classes and objects**
- Evolving a class progressively — from bare attributes to full OOP patterns
- Protecting data integrity with **encapsulation** and validation logic
- Reusing code through **inheritance** and avoiding duplication across subclasses
- Distinguishing **instance**, **class**, and **static** methods and when to use each
- Using **nested classes** to encapsulate internal subsystems (e.g. usage statistics)
- Building an **inheritance chain**: `Plant` → `Flower` → `Seed`

<p align="right"><a href="#-summary">⬆ back to summary</a></p>
</details>

---

<p align="left">
  Developed by <a href="https://github.com/jalves-de">Jonathan Alves</a>
</p>
