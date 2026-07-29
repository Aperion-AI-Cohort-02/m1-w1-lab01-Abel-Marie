# 📖 Lab01 Glossary - every word, one plain sentence

**The Cozy Bean · M1-W1-Lab01 · Aperion AI Training Academy**

*If a word in the lab stops making sense, it is here. In shop order first, then A-Z.*

---

## The story words

| Story | Python | Meaning |
|---|---|---|
| a labeled jar on the shelf | **variable** | a name holding one piece of information |
| what kind of jar it is | **data type** | the kind of thing a value is (number, text, yes/no) |
| repackaging a paper label | **casting** | converting a value from one type to another |
| the till | **operators** | the symbols that do maths and ask questions |
| the signboard and receipts | **strings** | text |
| the order queue | **list** | several things kept in order |
| a printed receipt | **tuple** | a list that cannot be changed |
| the menu on the wall | **dictionary** | pairs of name → value, looked up by name |
| the loyalty member list | **set** | a collection that refuses duplicates |
| a whiteboard vs ink on paper | **mutable vs immutable** | can be changed vs cannot be changed |

---

## A–Z

**argument** - a value you hand to a function inside its brackets. In `print("Hi")`, the argument is `"Hi"`.

**bool (boolean)** - a data type with only two possible values: `True` or `False`. Note the capital first letter.

**casting** - converting a value from one type to another, using `int()`, `float()` or `str()`.

**comment** - a line starting with `#`. A note for humans; Python ignores it completely.

**comparison operator** - a symbol that asks a question and answers `True` or `False`: `==`, `!=`, `>`, `<`, `>=`, `<=`.

**concatenation** - gluing pieces of text together with `+`. It adds no space unless you supply one.

**data type** - the kind of thing a value is. This lab uses four: `int`, `float`, `str`, `bool`.

**dictionary (`dict`)** - a container of `key: value` pairs, written in curly brackets, looked up by key rather than by position.

**f-string** - text with an `f` before the opening quote, where anything in `{curly brackets}` is replaced by its value.

**float** - a number with a decimal point, like `3.50`.

**function** - a named tool you use by writing brackets after its name, such as `print()`, `type()` or `len()`.

**immutable** - cannot be changed after it is created. Ink on printed paper. Strings and tuples are immutable.

**index** - the position number of an item in a list. **Counting starts at 0**, so the first item is at index `0`.

**int (integer)** - a whole number, with no decimal point, like `18`.

**`IndexError`** - the error you get when you ask for a position that does not exist, like `fruits[10]` in a four-item list.

**key** - the name half of a dictionary pair; the thing you look up with. Keys must be unique.

**`KeyError`** - the error you get when you ask a dictionary for a key it does not have.

**`len()`** - a built-in function that hands back how many items are in a list, set or piece of text.

**list** - several things kept in order, written in square brackets: `["Sara", "Ben"]`. Lists are mutable.

**literal** - a raw value typed straight into your code, like `12` or `"latte"`.

**logical operator** - `and`, `or`, `not` — used to combine or flip `True`/`False` answers.

**method** - a tool attached to a value, used with a dot: `"hello".upper()`. Same idea as a function, but it belongs to the value.

**modulo (`%`)** - the operator that hands back the remainder after division. `26 % 12` is `2`.

**mutable** - can be changed after it is created. A whiteboard. Lists, dictionaries and sets are mutable.

**`NameError`** - the error you get when you use a name Python has never been given, usually a typo or wrong capitalisation.

**operator** - a symbol that does something to values: `+`, `-`, `*`, `/`, `%`, `**`, `==`, `and`, and so on.

**precedence** - the order Python does arithmetic in: `*` and `/` before `+` and `-`; brackets first of all.

**`print()`** - the function that displays something on the screen. In a script, nothing appears without it.

**`range()`** - a function producing a run of numbers. `range(5)` gives 0, 1, 2, 3, 4 — it starts at 0 and stops *before* 5.

**script** - a file of Python instructions ending in `.py`, run with `python filename.py`.

**set** - a container that automatically refuses duplicates and keeps no order, written in curly brackets: `{1, 2, 3}`.

**slicing** - taking a run of items from a list with `[start:stop]`. The start is included, the stop is **not**.

**`snake_case`** - the naming style used in Python: all lowercase, words joined by underscores, like `cups_sold`.

**str (string)** - text, always written inside quotes: `"The Cozy Bean"`.

**`SyntaxError`** - the error you get when the grammar is wrong, usually a missing quote or bracket.

**terminal** - the text panel where you type commands like `python scripts/01_opening_day.py`.

**traceback** - the multi-line error report Python prints when something goes wrong. **Read its last line first.**

**tuple** - a list that cannot be changed, written in round brackets: `("latte", 3.50)`.

**`type()`** - a built-in function that tells you what data type a value is.

**`TypeError`** - the error you get when you use the wrong *kind* of thing, such as adding a number to text.

**value** - the contents half of a dictionary pair, or simply the thing stored in a variable.

**`ValueError`** - the error you get when a value is the right type but cannot be used, such as `int("forty-two")`.

**variable** - a name that holds one piece of information. A labeled jar.

**working directory** - the folder your terminal is currently standing in. Commands look for files here.


**`input()`** - a function that pauses the program, waits for you to type something, and hands back what you typed as text.

**`in`** - a keyword that asks whether something is inside a list, answering `True` or `False`.

**`.sort()`** - a list method that rearranges the list into order, in place.

**`.count()`** - a list method that says how many times something appears.

**`:.2f`** - a formatting instruction inside an f-string meaning "show exactly two digits after the decimal point", used to make numbers look like money.

