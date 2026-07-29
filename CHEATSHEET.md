# 📋 Lab01 Cheat Sheet - Python Basics

**The Cozy Bean · M1-W1-Lab01 · Aperion AI Training Academy**

*Everything from Lab01 on one page. Print it. Keep it beside your laptop. This page will outlive the lesson.*

---

## Running things

| What you want | What you type |
|---|---|
| Check Python is installed | `python --version` (Windows fallback: `py --version`) |
| See which folder you are in | `pwd` |
| See what is in this folder | `ls` |
| Go into a folder | `cd Lab01` |
| Run a script | `python scripts/01_opening_day.py` |
| Save your file | **Ctrl+S** (Windows) · **Cmd+S** (Mac) |

> ⚠️ Output did not change? **You did not save.** Look for the ● dot on the file tab.
>
> 📂 Always run from your `Lab01` folder (`AperionAI/Module1/Week1/Lab01`) — `pwd` should end in `Lab01`.

---

## Printing and comments

```python
print("Hello World")          # Hello World
print(3 * 3.50)               # 10.5
print("We sold", 18, "cups")  # We sold 18 cups   <- commas add spaces
# This line is a note. Python ignores it completely.
```

**In a script, nothing appears unless you `print()` it.**

---

## Variables - labeled jars

```python
cups_sold = 18          # label on the LEFT, contents on the RIGHT
cups_sold = 25          # refilling REPLACES; it never adds
```

- Names are **case-sensitive**: `cups_sold` and `Cups_Sold` are different jars.
- House style is **`snake_case`**: all lowercase, words joined by underscores.

---

## The four data types

| Type | Holds | Example | `type()` shows |
|---|---|---|---|
| `int` | whole number | `18` | `<class 'int'>` |
| `float` | decimal number | `3.50` | `<class 'float'>` |
| `str` | text, in quotes | `"The Cozy Bean"` | `<class 'str'>` |
| `bool` | `True` or `False` | `True` | `<class 'bool'>` |

```python
print(type(3.50))    # <class 'float'>
```

---

## Casting - repackaging between types

```python
float("3.50")   # 3.5   text  -> decimal
int("12")       # 12    text  -> whole number
str(18)         # "18"  number -> text
int(20.5)       # 20    CHOPS the decimal, does not round
```

---

## Arithmetic

| Op | Does | Example | Result |
|---|---|---|---|
| `+` | add | `10 + 5` | `15` |
| `-` | subtract | `10 - 5` | `5` |
| `*` | multiply | `10 * 5` | `50` |
| `/` | divide (**always decimal**) | `10 / 5` | `2.0` |
| `%` | remainder / leftovers | `26 % 12` | `2` |
| `**` | to the power of | `2 ** 3` | `8` |

**Precedence:** `*` `/` before `+` `-`; brackets jump the queue.

```python
2 + 3 * 5      # 17
(2 + 3) * 5    # 25
```

---

## Comparisons - always give `True` or `False`

```python
12.50 > 10     # True
12.50 == 10    # False    <- TWO equals asks a question
12.50 != 10    # True     <- "is different from"
```

> One `=` fills a jar. Two `==` asks a question. Never mix them up.

Also: `<`, `>=`, `<=`.

---

## Logic - combining questions

```python
is_member = True
big_order = 12.50 > 10

is_member and big_order   # True   <- BOTH must be true
is_member or big_order    # True   <- EITHER will do
not is_member             # False  <- flips it
```

**Name your questions.** `big_order = total > 10` reads far better than a wall of brackets.

---

## Strings - signs and receipts

```python
"Hello" + "Sara"          # HelloSara      <- no space added for you!
"Hello" + " " + "Sara"    # Hello Sara
3 * "Sara"                # SaraSaraSara

"grand opening".upper()   # GRAND OPENING
"GRAND".lower()           # grand
"Hello".replace("e","3")  # H3llo
```

**Multi-line text** - three quotes:

```python
board = """Today's specials:
  Latte    $3.50"""
```

**f-strings** - the modern way to slot values in:

```python
cups = 18
print(f"We sold {cups} cups")        # We sold 18 cups
print(f"Tomorrow: {cups + 10}")      # Tomorrow: 28   <- maths works inside {}
print("Welcome to {}!".format("The Cozy Bean"))
```

> 🚀 Bonus: `f"${total:.2f}"` → `$63.00` (money with 2 decimals).

---

## Lists - the order queue

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

queue[0]           # Sara      <- FIRST is position 0
queue[-1]          # Marcus    <- last, counting from the back
len(queue)         # 4
queue[1:3]         # ['Ben', 'Aisha']   <- stops BEFORE 3
queue.append("Priya")   # adds to the end
queue.remove("Ben")     # removes by name
queue[0] = "Dev"        # lists are MUTABLE -- rewrite in place
list(range(5))          # [0, 1, 2, 3, 4]   <- starts at 0, stops before 5
```

> 🚀 Bonus: `"Sara" in queue` → `True`/`False` · `names.sort()` · `queue.count("Dev")`

---

## Mutability - the one picture

| | Picture | Examples |
|---|---|---|
| **Mutable** | a **whiteboard** — wipe and rewrite | lists, dictionaries, sets |
| **Immutable** | **ink on printed paper** — print a new one | strings, tuples |

---

## Tuples - the printed receipt

```python
receipt = ("latte", 3.50, "Sara")   # round brackets
receipt[0]                          # latte    <- reading is fine
receipt[0] = "tea"                  # TypeError -- cannot be changed
```

---

## Dictionaries - the menu

```python
menu = {"latte": 3.50, "espresso": 2.75}

menu["latte"]                  # 3.5    <- look up by NAME, not position
menu["hot chocolate"] = 3.25   # new key   -> added
menu["latte"] = 3.75           # existing  -> replaced
menu.keys()                    # dict_keys([...])
menu.values()                  # dict_values([...])
```

---

## Sets - the member list

```python
{1, 2, 3, 4, 5, 5}                    # {1, 2, 3, 4, 5}  <- duplicate dropped
len(set(["Sara","Ben","Sara"]))       # 2
```

No duplicates, no order, no indexing.

---

## Errors you have met (and can now read)

| Error | Means | Typical cause |
|---|---|---|
| `NameError` | no jar has that label | typo or wrong capitals |
| `TypeError` | wrong *kind* of thing | `10 + "20"`, or editing a tuple |
| `ValueError` | right kind, unusable value | `int("forty-two")` |
| `IndexError` | that position does not exist | `fruits[10]` on a 4-item list |
| `KeyError` | no such key in the dictionary | `menu["tea"]` when you sell no tea |
| `SyntaxError` | a typo in the grammar | missing quote or bracket |

> **Always read the LAST line of an error first.** That is where Python says what actually went wrong. The wall of text above it is just the trail showing where it happened.

