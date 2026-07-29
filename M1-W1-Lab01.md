# ☕ M1-W1-Lab01 - Opening Week at The Cozy Bean

### Python Basics · Aperion AI Training Academy
*"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 1 |
| **Lab** | Lab01 - Opening Week at The Cozy Bean |
| **Duration** | **≈ 1 hour** of lab work (one-time setup **not** counted) |
| **Difficulty** | ⭐ Absolute Beginner - no experience assumed, none at all |

> 🛋️ **Aim for one sitting of about an hour.** If you do need to pause, stop after any 🧠 Quick Quiz — that is always a clean break. Your shop will still be here tomorrow.

### What you learned in class (and will now make your own)

What Python is · your first program · Python as a calculator · variables · data types (`int`, `float`, `str`, `bool`) · casting · type errors · arithmetic operators · comparison operators · logical operators · strings and f-strings · `print()` and comments · lists, indexing and slicing · mutability · tuples · dictionaries · sets

---

## 1. ☕ The Story

You did it. You signed the lease.

It is a narrow little corner shop with a wobbly third table and a window that catches the morning sun, and from Monday it is **The Cozy Bean** - your coffee shop. The espresso machine is polished. The jars on the shelf behind the counter are empty and waiting. There is a brand-new till, a chalkboard, and a stack of loyalty cards nobody has stamped yet.

There is just one problem: you are one person, and by 8:15 a.m. on Monday there will be a queue.

So you have hired some help. Not a barista - a **programming language**. Python is going to be the quiet, tireless assistant who remembers how many cups you sold, works out the change, keeps the menu, tracks the queue, and never once asks for a day off. This week you are going to teach it how your shop works.

Here is the lovely part: everything Python does has a physical twin behind your counter. A **variable** is a labeled jar. A **list** is the queue of customers. A **dictionary** is the menu on the wall. A **tuple** is a printed receipt you cannot scribble on. Learn the shop, and you have learned Python. That is the whole trick, and by Friday it will feel obvious.

### Why this matters in real life (and in AI/ML)

- **Every data job starts here.** Before anyone trains a model, somebody puts numbers in labeled containers and checks their types. Numbers that arrive as text - exactly what you will meet in STEP 7 - are the single most common bug in real data work.
- **AI is this, at scale.** A machine-learning pipeline is jars, tills and queues with a great many more of them. The ideas do not change; the numbers just get bigger.
- **Reading errors is the actual daily skill.** Professional engineers do not avoid errors, they read them. In this lab you will trigger four errors *on purpose* and learn to translate them. That habit will serve you for years.

### ✅ Success Criteria - what you will be able to produce

By the end of this lab you will be able to run every one of these and understand every line:

- `python scripts/01_opening_day.py` - your first program, and the till doing maths
- `python scripts/02_labeled_jars.py` - values stored in well-named variables, with their types
- `python scripts/03_repackaging.py` - text converted to numbers, plus two errors you can explain
- `python scripts/04_the_till.py` - arithmetic, comparisons, and a real counter rule
- `python scripts/05_signboards.py` - signs and receipts built out of text
- `python scripts/06_order_queue.py` - a customer queue you can add to, serve from, and slice
- `python scripts/07_menus_members.py` - a working menu and a duplicate-free member list
- 🚀 `python scripts/08_bonus_take_an_order.py` - *(bonus)* a till that takes an order you type in
- …and seven practice problems solved in your own words, in `practice/`.

---

## 2. 🎯 Learning Objectives

By the end of this lab you will be able to:

1. Say what Python is, and run a Python program of your own.
2. Use Python as a calculator, and store results in **variables** with good names.
3. Name the four basic **data types** and check any value with `type()`.
4. Convert between types with `int()`, `float()` and `str()` - and read the errors that appear when you cannot.
5. Use arithmetic, comparison and logical operators to work out real answers.
6. Build text for signs and receipts, including **f-strings**.
7. Manage a **list**: index it from zero, slice it, add to it and remove from it.
8. Explain what **mutable** and **immutable** mean, using something you can picture.
9. Use **tuples**, **dictionaries** and **sets**, and say when each one is the right container.

---

## 3. 🔧 Before You Start (one-time setup - not counted in the 1 hour)

Take your time here. Everyone does this once, and then never again.

> 🎁 **You never create a file in this lab.** Every file you need is already in the lab folder. You only ever *open*, *edit*, *save* and *run* files. (Later, in Lab02, some of your programs will create files - but that is Python doing it for you, not you making them by hand.)

> 📥 **Not cloned this lab yet?** The [README](README.md#1--get-this-repo-onto-your-computer) walks you through it: click the GitHub Classroom link from Google Classroom, copy your own repo address, and clone it into `AperionAI/Module1/Week1/Lab01`. Do that first — everything below assumes the folder is on your computer.

### 3.1 Do you have Python?

Open a terminal (the next section shows you how) and type this, then press Enter:

```text
python --version
```

You should see something like `Python 3.14.3`. Anything starting with **3.10 or higher** is perfect.

- **Nothing happens, or you see "not recognized"?** On Windows, try `py --version` instead. If that also fails, install Python from [python.org/downloads](https://www.python.org/downloads/) — and on the very first installer screen, **tick the box that says "Add python.exe to PATH"**. That one tick prevents the most common beginner setup problem in the world.
- **On a Mac?** Use `python3 --version` if `python` is not found. If it is missing, install from the same page.

### 3.2 Opening VS Code and a terminal

**VS Code** is a free text editor - think of it as Microsoft Word for code. Download it from [code.visualstudio.com](https://code.visualstudio.com/) if you do not have it.

**The single easiest route (do it this way):**

1. Open VS Code.
2. Click **File → Open Folder…**
3. Choose your **`Lab01`** folder - the one you cloned, at `AperionAI/Module1/Week1/Lab01`. It is the folder containing this document. Click Select Folder / Open.
4. On the left you will now see a panel listing `scripts`, `practice`, `solutions` and this file. That panel is called the Explorer.
5. Click **Terminal → New Terminal** in the top menu. A black-ish panel opens along the bottom of the window with a blinking cursor.

That terminal is now *already standing inside your lab folder* — which is exactly where every command in this lab needs to be run from.

### 3.3 What is a "working directory"?

Imagine you are standing in a room in a big building. If you shout *"pass me the menu!"*, whoever is **in that room** hands it to you. If you are standing in the wrong room, nobody answers.

Your terminal is always standing in exactly one folder. That folder is the **working directory** - the room it is standing in. When you ask it to run `scripts/01_opening_day.py`, it looks for a `scripts` folder **in the room it is currently standing in**. If it is standing somewhere else, it will honestly tell you it cannot find the file.

**To check which room you are in:**

```text
pwd
```

The answer should end in `Week1/Lab01` — Windows shows it with backslashes, `...\Week1\Lab01`. (On Windows PowerShell, `pwd` works too.)

**To see what is in the room with you:**

```text
ls
```

You should see at least `README.md`, `M1-W1-Lab01.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `scripts`, `practice` and `solutions`.

**If you are in the wrong room**, walk to the right one with `cd` (it stands for "change directory"), then check again:

```text
cd "Lab01"
pwd
```

Honestly though - using **File → Open Folder** puts you in the right room automatically, every time. Prefer that.

### 3.4 Opening, editing and - please - **saving**

1. In the Explorer panel on the left, click `scripts`, then click `01_opening_day.py`. It opens in the big area on the right.
2. Change something - anything. Change `Hello World` to `Hello Coffee`.
3. Look at the **file tab** at the top. See the small **● dot** where the little ✕ usually is? That dot means **"this file has unsaved changes."**
4. Press **Ctrl+S** (Windows) or **Cmd+S** (Mac). The dot turns back into an ✕. Your change is now real.

> ### ⚠️ THE MOST COMMON BEGINNER PROBLEM IN THE WORLD
>
> **Changed the code but the output didn't change? You probably didn't save - look for the dot on the file tab, press Ctrl+S / Cmd+S, and rerun.**
>
> Nine times out of ten, this is the answer. Not a broken computer. Not a broken you. Just an unsaved file. Check this *first*, every single time.

### 3.5 Running a script

In the terminal, type this and press Enter:

```text
python scripts/01_opening_day.py
```

You should see:

```text
Hello World
Welcome to The Cozy Bean!
10.5
12.75
648.56402
```

That is it. That is running a program. Windows and Mac use the exact same command.


### 3.6 "If you see this error, do this"

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError` / `can't open file` / `No such file or directory` | **You are running from the wrong folder.** | Type `pwd`. Does it end in `Lab01`? If not, use **File → Open Folder** on your `Lab01` folder and open a fresh terminal, or `cd` into it. Then type `ls` and check you can see the `scripts` folder. |
| `'python' is not recognized…` | Windows cannot find Python. | Try `py scripts/01_opening_day.py` instead. If that fails, reinstall Python with "Add python.exe to PATH" ticked. |
| `command not found: python` (Mac) | Mac calls it something else. | Use `python3 scripts/01_opening_day.py`. |
| Output did not change after an edit | The file was never saved. | Look for the ● dot on the tab. Ctrl+S / Cmd+S. Rerun. |
| `SyntaxError` | A typo — a missing quote or bracket. | Read the line number in the message, then look at **that line and the one above it**. Usually a quote or bracket is missing its partner. |
| `IndentationError` | Spacing at the start of a line is wrong. | Not needed in Lab01 — but you will meet it properly in Lab02. |

---

## 4. 📖 Guided Walkthrough

Twenty-eight small steps, in seven groups. Each group has one script in `scripts/` you can run to see everything in that group working together.

**How to use each STEP:** read it, run the matching script, compare your output to the 📺 block, then do the 🎤 30-second tweak. That tweak is not optional decoration - it is the moment the idea moves from "I read that" to "I can do that."

---

## ☕ Welcome Page - What even *is* Python?

Before the first STEP, ninety seconds of background. No code, no pressure.

**Python is a programming language** - a set of written instructions a computer will follow. You write them in plain-ish English; Python does exactly what they say, in order, every time.

Four things worth knowing about it:

- **It is interpreted.** Python reads your instructions **one line at a time and runs each one as it goes** - like a cook reading a recipe card step by step. Some other languages must be "built" into a finished program first, in a separate step, before anything can run. Python skips that. You write a line, you run it, you see it work. That is why it is such a kind language to learn on.
- **It is beginner-friendly.** The grammar is small and reads close to English. You will be writing real, working programs within the hour.
- **It is free**, and always has been. Free to download, free to use, free forever, including commercially.
- **It powers modern AI.** Nearly every AI and machine-learning system you have heard of is built with Python. The very same `print()` you are about to write is used at those companies every day.

> 😄 **Fun fact:** Python is not named after the snake. Its inventor, Guido van Rossum, was a fan of the British comedy troupe **Monty Python's Flying Circus**, and named his language after them in 1991. Which is why Python's official documentation has, for thirty years, been quietly full of spam, eggs, and silly jokes.

---

## ☕ Cluster A - Opening Day

*Script for this cluster:* **`scripts/01_opening_day.py`**

The key is in the door. Let us turn on the lights.

---

### STEP 1 - Your very first program

▶ *In your script:* Section 1 of `scripts/01_opening_day.py`

🎯 **Objective:** Make the computer say something out loud.

☕ **Story moment:** Every shop has a ribbon-cutting. Yours is one line long. Before the coffee, before the customers, you flip on the till and it prints its very first line of receipt paper — proof that the whole thing is alive.

🧠 **The idea in plain English:** `print()` is Python's way of putting words on the screen. You write `print`, then round brackets, then whatever you want shown. Text goes inside quotes so Python knows it is words rather than an instruction. `print` is a **function** — a named tool you use by putting brackets after its name. It is the first of many.

💻 **The code:**

```python
print("Hello World")
print("Welcome to The Cozy Bean!")
```

📺 **Expected output:**

```text
Hello World
Welcome to The Cozy Bean!
```

⚠️ **Common mistake:** Forgetting the quotes. `print(Hello World)` makes Python think `Hello` is the name of something you stored earlier — and it will tell you it has never heard of it. **Words need quotes. Always.**

✅ **Verify:** Two lines on screen, in that order. That is a working program. You are, as of right now, a person who has written software.

🎤 **Try it yourself (30 seconds):** Change `The Cozy Bean` to whatever *you* would name a coffee shop. Save (Ctrl+S). Rerun. Your shop, your sign.

> 📌 **You saw this in class:** `print("Hello World")` was the very first thing your instructor ran — it is the traditional first program in every language, written by millions of people before you. You are in good company.

---

### STEP 2 - The till is a calculator

▶ *In your script:* Section 2 of `scripts/01_opening_day.py`

🎯 **Objective:** Do real arithmetic with Python.

☕ **Story moment:** Before Python knows anything about *your* shop, it already knows maths. Your first customer wants three lattes at $3.50. Rather than reaching for a calculator, you ask the till.

🧠 **The idea in plain English:** Put a sum inside `print()` and Python works it out before showing you the answer. `*` means multiply and `+` means add. No quotes this time — quotes would make it *text*, and Python does not do arithmetic on text.

💻 **The code:**

```python
# Three lattes at $3.50 each
print(3 * 3.50)

# Those three lattes plus one muffin at $2.25
print(3 * 3.50 + 2.25)
```

📺 **Expected output:**

```text
10.5
12.75
```

⚠️ **Common mistake:** Wrapping the sum in quotes. `print("3 * 3.50")` prints the literal characters `3 * 3.50` instead of `10.5` — you asked for a photograph of a sum, not the sum. Quotes mean "treat this as words."

✅ **Verify:** `10.5` and `12.75`. Note that Python writes `10.5`, not `10.50` — it never shows a trailing zero it does not need. The value is identical; only the display differs. (You will make it look like proper money in STEP 17.)

🎤 **Try it yourself (30 seconds):** Change `3` lattes to `7` lattes. Save, rerun. Do you get `24.5`?

> 📌 **You saw this in class:** the London-to-Edinburgh conversion. Your bean supplier drives that exact route — 403 miles — and one mile is 1.60934 km:
>
> ```python
> print(403 * 1.60934)
> ```
>
> ```text
> 648.56402
> ```

---

### 🧠 Quick Quiz #1 — answer from memory, before peeking

*(Answers are in the **Answer Key** at the end of this lab. No scrolling ahead. Wrong guesses are genuinely useful — being wrong and then finding out is one of the strongest ways to make something stick.)*

**Q1.** What does `print("Hello World")` make the computer do?

- A) Stores the words for later use
- B) Sends the words to a printer
- C) Turns the words into a number
- D) Shows the words on the screen

**Q2.** What does `print(403 * 1.60934)` show?

- A) `403 * 1.60934`
- B) `403`
- C) `648.56402`
- D) an error message

---

## ☕ Cluster B — Variables Are Labeled Jars

*Script for this cluster:* **`scripts/02_labeled_jars.py`**

Behind your counter is a big wooden shelf. This morning it is empty. By the end of this cluster it will hold neatly labeled jars — and you will understand the single most important idea in all of programming.

---

### STEP 3 — Your first labeled jar

▶ *In your script:* Section 1 of `scripts/02_labeled_jars.py`

🎯 **Objective:** Store a value in a variable — and see that refilling a jar *replaces* what was inside.

☕ **Story moment:** Your first delivery arrives: a sack of coffee beans. You pour 12 scoops into a glass jar, grab the label maker, and stick `beans_in_stock` on the front. Now anyone — including you at 6 a.m. — can glance at the shelf and know what is in there. When the bigger afternoon delivery lands, you do not grab a second jar. You refill this one.

🧠 **The idea in plain English:** A **variable** is a labeled jar holding one piece of information. The name is the label; the value is the contents. The `=` sign means *"put this into that jar"* — it is **not** the "equals" from maths class. And one rule of the shelf: a jar holds exactly **one** thing at a time. Filling it again *replaces* what was there. It never adds.

💻 **The code:**

```python
# Put the number 12 into a jar labeled beans_in_stock
beans_in_stock = 12
print(beans_in_stock)

# The afternoon delivery arrives -- refill the SAME jar
beans_in_stock = 50
print(beans_in_stock)
```

📺 **Expected output:**

```text
12
50
```

⚠️ **Common mistake:** Writing the value first. `12 = beans_in_stock` stops Python on the spot:

```text
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

In plain English: a **literal** is a raw value like `12`, and Python is pointing out that you cannot pour a jar into a number. **The label goes on the LEFT of `=`, the contents on the RIGHT.**

✅ **Verify:** `12`, then `50`. The afternoon delivery *replaced* the morning one — it did not add up to 62.

🎤 **Try it yourself (30 seconds):** Change `50` to `200` (a truly enormous delivery). Save, rerun. The second line becomes `200`. If it still says `50` — you did not save. 😉

---

### STEP 4 — Let the jars do the maths

▶ *In your script:* Section 2 of `scripts/02_labeled_jars.py`

🎯 **Objective:** Use stored variables inside new calculations.

☕ **Story moment:** Closing time on day one. The chalkboard says 18 cups at $3.50 each. Rather than punching raw numbers into the till, you use the jars — because tomorrow the numbers will change, but the *recipe for the maths* will not.

🧠 **The idea in plain English:** Once a jar is on the shelf, you can use its name anywhere and Python quietly swaps in the value. You can even fill a brand-new jar with the *result* of maths done on other jars.

💻 **The code:**

```python
cups_sold = 18
price = 3.50

money_today = cups_sold * price

print(money_today)
print(cups_sold + 4)   # 4 free cups for the builders next door
```

📺 **Expected output:**

```text
63.0
22
```

⚠️ **Common mistake:** Typing the raw numbers again (`18 * 3.50`) instead of using the jars. It works today — but tomorrow you will be hunting for every `18` hidden across your code. Change a jar once, and everything using it updates itself.

✅ **Verify:** `63.0` then `22`. Notice `63.0` has a decimal point while `22` does not — hold that thought, STEP 6 explains exactly why.

🎤 **Try it yourself (30 seconds):** Tomorrow you sell 25 cups. Change **only** the `cups_sold` jar. Save, rerun. `money_today` updates all by itself — that is the entire point of jars.

> 📌 **You saw this in class:** the very first variables your instructor made stored the London↔Edinburgh trip for our bean supplier:
>
> ```python
> distance_to_london_miles = 403
> mile_to_km = 1.60934
>
> distance_london_edinburgh_km = distance_to_london_miles * mile_to_km
>
> print(distance_london_edinburgh_km)
> ```
>
> ```text
> 648.56402
> ```
>
> Three jars: two you fill yourself, and a third filled by maths done on the other two.

---

### STEP 5 — Capital letters make different jars

▶ *In your script:* Section 3 of `scripts/02_labeled_jars.py`

🎯 **Objective:** Learn that variable names are case-sensitive, and adopt `snake_case` so it never bites you.

☕ **Story moment:** Your cousin "helps out" on day two and labels a new jar `Cups_Sold`, with fancy capitals. Now there are **two** jars on the shelf and the morning count does not match the evening count. The shop needs one labeling style, and it needs it today.

🧠 **The idea in plain English:** Labels are **case-sensitive**: `cups_sold` and `Cups_Sold` are two completely different jars, even though they read identically out loud. Python programmers avoid the whole problem by writing every label in **`snake_case`** — all lowercase, words joined by underscores. One style, no surprises.

💻 **The code:**

```python
cups_sold = 18
Cups_Sold = 99   # a DIFFERENT jar -- the capitals matter!

print(cups_sold)
print(Cups_Sold)
```

📺 **Expected output:**

```text
18
99
```

⚠️ **Common mistake:** Asking for a jar that does not exist. If only `cups_sold` is on the shelf and you type `print(Cups_Sold)`, Python prints an error report. That report is called a **traceback**, and the trick is to **read its last line first**:

```text
Traceback (most recent call last):
  File "your_file.py", line 2, in <module>
    print(Cups_Sold)
          ^^^^^^^^^
NameError: name 'Cups_Sold' is not defined. Did you mean: 'cups_sold'?
```

`NameError` is Python's polite way of saying *"no jar on my shelf has that exact label."* Recent versions of Python even guess which jar you meant. (Where it says `File "your_file.py"`, your screen will show your own folder path — that part is normal and nothing to worry about.)

✅ **Verify:** `18` then `99` — living proof they are two separate jars.

🎤 **Try it yourself (30 seconds):** Delete the `Cups_Sold = 99` line, save, and rerun to meet your first `NameError` face to face. Read the last line. Then put the line back.

> 📌 **From the class session:** the marathon example was written `marathonMiles` and `marathonKm`, with capital letters in the middle. Python allows that style, and you will see it in the wild. **This course uses `snake_case`** — so in your script it appears as `marathon_miles` and `marathon_km`. Same maths, house style:
>
> ```python
> marathon_miles = 26.2
> marathon_km = marathon_miles * mile_to_km
> print("Marathon distance in km:", marathon_km)
> ```
>
> ```text
> Marathon distance in km: 42.164708
> ```

---

### STEP 6 — Four kinds of jars (data types)

▶ *In your script:* Section 4 of `scripts/02_labeled_jars.py`

🎯 **Objective:** Meet `int`, `float`, `str` and `bool`, and check any jar with `type()`.

☕ **Story moment:** Not everything in the shop is a scoop count. Some jars hold prices with cents. One holds the shop's name, painted on the glass. One holds the little sign hanging on the door: OPEN or CLOSED. Different contents — different *kinds* of jar.

🧠 **The idea in plain English:** Every value has a **data type**, meaning the kind of thing it is. Four you will use constantly:

| Type | What it holds | Example |
|---|---|---|
| `int` | a whole number | `18` |
| `float` | a number with a decimal point | `3.50` |
| `str` | text, always inside quotes | `"The Cozy Bean"` |
| `bool` | only `True` or `False` | `True` |

To check a jar, use `type()` — a **function**, meaning a named tool you run by putting brackets after its name (`print()` was your first). `type()` reads the fine print on any jar for you.

💻 **The code:**

```python
cups_sold = 18                  # int   -- a whole number
price = 3.50                    # float -- has a decimal point
shop_name = "The Cozy Bean"     # str   -- text, in quotes
is_open = True                  # bool  -- True or False, capital first letter

print(type(cups_sold))
print(type(price))
print(type(shop_name))
print(type(is_open))
```

📺 **Expected output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

⚠️ **Common mistake:** Quotes silently turn things into text. `price = "3.50"` is a `str` — a *photograph of a number* — and you cannot do arithmetic with a photograph. The whole of Cluster C is about fixing exactly this.

✅ **Verify:** Four lines, each `<class '…'>`. That slightly odd costume is just how Python says "this is an int."

🎤 **Try it yourself (30 seconds):** Add a fifth jar, `muffins_left = 0`, and print its type. A whole number — so which of the four will it be? Predict first, then check.

> 📌 **You saw this in class:**
>
> ```python
> # Assigning values to variables
> x = 10             # Integer
> y = 20.5           # Float
> name = "Debela"    # String
> is_active = True   # Boolean
> ```
>
> ```text
> (no output -- these lines only fill jars; nothing appears without print())
> ```
>
> The same four types, moved onto your shop shelf.

---

### 🧠 Quick Quiz #2 — answer from memory, before peeking

**Q1.** After these two lines run, what is in the jar?

```python
cups_sold = 18
cups_sold = 25
```

- A) `18`
- B) `25`
- C) `43`
- D) `error`

**Q2.** What does `type(3.50)` return?

- A) `<class 'int'>`
- B) `<class 'str'>`
- C) `<class 'bool'>`
- D) `<class 'float'>`

**Q3.** Only `cups_sold = 18` has run. What does `print(Cups_Sold)` do?

- A) It prints `18`
- B) It prints `0`
- C) It raises a `NameError`
- D) It raises a `SyntaxError`

---

## ☕ Cluster C — Repackaging (casting)

*Script for this cluster:* **`scripts/03_repackaging.py`**

This cluster is where most beginners get quietly stuck for a week. You are going to get it in twenty minutes, because you have a shelf to think with.

---

### STEP 7 — The supplier writes prices on paper

▶ *In your script:* Section 1 of `scripts/03_repackaging.py`

🎯 **Objective:** Convert between text and numbers with `float()`, `int()` and `str()`.

☕ **Story moment:** The bean delivery arrives with the price written on a paper label stuck to the sack: `3.50`. To you it looks like a number. To Python it is *text* — a picture of a number, no more useful for arithmetic than the word "three". Before you can do any maths, you have to repackage it.

🧠 **The idea in plain English:** **Casting** means converting a value from one type to another. Three tools do almost all the work:

- `float("3.50")` → text becomes a decimal number
- `int("12")` → text becomes a whole number
- `str(18)` → a number becomes text (for signs and receipts)

💻 **The code:**

```python
price_label = "3.50"        # arrives as TEXT -- note the quotes
print(type(price_label))

price = float(price_label)  # repackaged into a real number
print(type(price))
print(price * 2)            # now maths works
```

📺 **Expected output:**

```text
<class 'str'>
<class 'float'>
7.0
```

⚠️ **Common mistake:** Assuming that because it *looks* like a number, it *is* one. `"12" + "3"` gives `"123"` — because gluing two pieces of text together is exactly what `+` does to text. Check with `type()` whenever a value comes from outside your program.

✅ **Verify:** `str` first, then `float`, then `7.0`. The `.0` is your proof it became a real number.

🎤 **Try it yourself (30 seconds):** Change the label to `"4.25"` and rerun. Do you get `8.5`?

**The other direction**, from the same script:

```python
bags = int("12")
print(bags + 3)

cups = 18
print("We sold " + str(cups) + " cups")

print(int(20.5))
```

```text
15
We sold 18 cups
20
```

Note that last one: `int(20.5)` gives `20`, not `21`. **It chops the decimal off; it does not round.** Handy to know before you count anybody's money.

---

### STEP 8 — Your first error, on purpose 🎉

▶ *In your script:* Section 2 of `scripts/03_repackaging.py` (commented out, so the script still runs clean)

🎯 **Objective:** Trigger a `TypeError`, read it, and translate it.

☕ **Story moment:** You try to add 10 cups of stock to a paper label that says `"20"`. The till simply refuses. It is not being difficult — it genuinely cannot tell whether you want `30` (the sum) or `1020` (the two glued together), so it stops and asks.

🧠 **The idea in plain English:** Python will not add a number to text. Rather than guess what you meant, it stops and says so. **This is a feature.** A language that guessed here would eventually cost somebody a lot of money.

💻 **The code** (in your script this sits inside a comment — uncomment it to see it live):

```python
x = 10
y = "20"
print(x + y)
```

📺 **Expected output** — a real error, captured by running exactly this in a terminal:

```text
Traceback (most recent call last):
  File "your_file.py", line 3, in <module>
    print(x + y)
          ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Translated into plain English:** *"You used `+` between an `int` and a `str`. I do not know how to do that."* The little `~~^~~` marks are Python pointing at the exact spot that upset it.

**And the fix** — repackage first, then add:

```python
print(x + int(y))
```

```text
30
```

⚠️ **Common mistake:** Panicking at the wall of text. Do not read a traceback top to bottom. **Read the last line first** — it names the problem. Then glance up for the line number.

✅ **Verify:** With the error lines commented out, `python scripts/03_repackaging.py` runs clean and prints `30` among its output. Uncomment them to meet the error in person, then comment them back.

🎤 **Try it yourself (30 seconds):** Uncomment those three lines, save, and run it. Read the last line out loud. Then put the `#` marks back.

> 📌 **You saw this in class:** this exact demo — `x = 10`, `y = "20"`, `x + y`. Your instructor triggered it deliberately, for exactly this reason.

---

### STEP 9 — The second error, also on purpose

▶ *In your script:* Section 3 of `scripts/03_repackaging.py`

🎯 **Objective:** Trigger a `ValueError` and see how it differs from a `TypeError`.

☕ **Story moment:** A supplier scribbles *"about three fifty"* on the label instead of `3.50`. You hand it to the till and ask for a number. The till is willing — it just cannot find a number in there.

🧠 **The idea in plain English:** `int()` is happy to convert text, **but only text that genuinely looks like a number**. Give it words and it will tell you plainly. Note the difference: a `TypeError` means *"wrong kind of thing"*; a `ValueError` means *"right kind of thing, but I cannot use this particular value."*

💻 **The code:**

```python
print(int("Python is powerful."))
```

📺 **Expected output** — real, captured from a terminal:

```text
Traceback (most recent call last):
  File "your_file.py", line 1, in <module>
    print(int("Python is powerful."))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Python is powerful.'
```

**Translated:** *"You asked me to turn this text into a whole number, but there is no number in it."* ("base 10" just means ordinary counting numbers — you can ignore it.)

**And what works:**

```python
print(int("42"))
```

```text
42
```

⚠️ **Common mistake:** Assuming empty text is zero. `int("")` fails too — there is no number in nothing.

✅ **Verify:** The script prints `42` and exits cleanly; the error only appears if you uncomment the demo line.

🎤 **Try it yourself (30 seconds):** Try `int("3.50")` in the script. It fails too! Can you say why before reading on? *(Because `3.50` is not a **whole** number — `float("3.50")` is what you want.)*

---

### 🧠 Quick Quiz #3 — answer from memory, before peeking

**Q1.** Which one of these lines fails?

- A) `int("forty-two")`
- B) `int("42")`
- C) `float("3.50")`
- D) `str(42)`

**Q2.** `x = 10` and `y = "20"`. What does `x + y` do?

- A) It gives `30`
- B) It raises a `TypeError`
- C) It gives `1020`
- D) It raises a `ValueError`

**Q3.** What does `str(42)` hand back?

- A) The number `42`
- B) The number `4.2`
- C) An error
- D) The text `"42"`

---

## ☕ Cluster D — The Till

*Script for this cluster:* **`scripts/04_the_till.py`**

Time to ring up some actual orders, and to teach the shop its first rule.

---

### STEP 10 — The four everyday operators

▶ *In your script:* Section 1 of `scripts/04_the_till.py`

🎯 **Objective:** Add, subtract, multiply and divide.

☕ **Story moment:** The morning rush. Orders come in, the till adds them up, change goes back. Nothing exotic — just the four operations you have known since school, spelled slightly differently.

🧠 **The idea in plain English:** `+` adds, `-` subtracts, `*` multiplies, `/` divides. One surprise worth knowing now: **`/` always gives you a decimal**, even when the answer is a whole number.

💻 **The code:**

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

📺 **Expected output:**

```text
15
5
50
2.0
```

⚠️ **Common mistake:** Being surprised by `2.0` instead of `2`. Division always hands back a `float`. That is Python being consistent, not Python being wrong.

✅ **Verify:** Four numbers, and the last one has a `.0`.

🎤 **Try it yourself (30 seconds):** Change `b` to `4` and rerun. `10 / 4` should give `2.5`.

---

### STEP 11 — Leftovers, powers, and who goes first

▶ *In your script:* Section 2 of `scripts/04_the_till.py`

🎯 **Objective:** Use `%` and `**`, and learn the order of precedence.

☕ **Story moment:** You baked 26 muffins and box them by the dozen. Two full boxes… and some left over for the staff. Meanwhile the "double double double" promo doubles a drink three times over. And the till, quietly, has firm opinions about which sum to do first.

🧠 **The idea in plain English:** `%` (called *modulo*) hands back **what is left over** after dividing. `**` raises a number to a power. And precedence works exactly as it did in school: **multiplication and division happen before addition and subtraction**, and brackets jump the queue entirely.

💻 **The code:**

```python
muffins_baked = 26
print(muffins_baked % 12)   # leftovers after boxing by the dozen

print(2 ** 3)               # 2 doubled, doubled, doubled

print(2 + 3 * 5)            # 3*5 happens first
print((2 + 3) * 5)          # brackets go first
```

📺 **Expected output:**

```text
2
8
17
25
```

⚠️ **Common mistake:** Expecting `2 + 3 * 5` to be `25` because you read left to right. Python does not read left to right for arithmetic — it follows precedence. **When in doubt, add brackets.** They cost nothing and they say exactly what you mean.

✅ **Verify:** `2`, `8`, `17`, `25`. Those last two are the same digits in the same order producing different answers — that is precedence in one glance.

🎤 **Try it yourself (30 seconds):** You baked 30 muffins. Change the number and rerun — how many are left after boxing by the dozen?

> 📌 **You saw this in class:** `2 + 3 * 5` = **17** versus `(2 + 3) * 5` = **25**. Exactly the same example.

---

### STEP 12 — Questions with yes/no answers

▶ *In your script:* Section 3 of `scripts/04_the_till.py`

🎯 **Objective:** Use comparison operators that hand back `True` or `False`.

☕ **Story moment:** At the counter you constantly ask small yes/no questions. Is this order over $10? Is the muffin tray empty? Is this the same customer as yesterday? Each has exactly two possible answers.

🧠 **The idea in plain English:** A **comparison** always hands back `True` or `False` — never a number.

| Operator | Asks |
|---|---|
| `==` | are these two the same? |
| `!=` | are these two different? |
| `>` `<` | is this bigger / smaller? |
| `>=` `<=` | bigger-or-equal / smaller-or-equal? |

Note the double `==`. One `=` fills a jar; two `==` asks a question. Python cares a great deal about the difference.

💻 **The code:**

```python
order_total = 12.50

print(order_total > 10)       # is it a big order?
print(order_total < 10)       # is it a small order?
print(order_total == 10)      # is it exactly ten?
print(order_total != 10)      # is it different from ten?
print(order_total >= 12.50)   # at least this much?
print(order_total <= 12.50)   # at most this much?
```

📺 **Expected output:**

```text
True
False
False
True
True
True
```

Look at those last two: `12.50` is **not** greater than `12.50`, but it *is* greater-than-**or-equal-to** it — so `>=` and `<=` are both `True` at the same time. That is what the "or equal to" half buys you.

⚠️ **Common mistake:** Writing `=` when you mean `==`. `order_total = 10` does not ask a question — it *overwrites* the jar with 10, silently destroying your data. This is one of the most expensive typos in programming.

✅ **Verify:** Six answers: `True`, `False`, `False`, `True`, `True`, `True` — with capital first letters, which is how Python spells them.

🎤 **Try it yourself (30 seconds):** Change `order_total` to `7.00` and rerun. Every answer flips in a way you can predict. Predict first, then check!

---

### STEP 13 — Combining rules at the counter

▶ *In your script:* Section 4 of `scripts/04_the_till.py`

🎯 **Objective:** Combine questions with `and`, `or` and `not`.

☕ **Story moment:** Here is your shop's first real rule: **a free cookie if you are a loyalty member AND your order is over $10.** Two conditions, both required. Say it out loud and you have already written it — Python spells it almost identically.

🧠 **The idea in plain English:** `and` needs **both** sides True. `or` needs **at least one** side True. `not` flips True into False and back. Best habit: give each question its own well-named jar, so the final rule reads like English.

💻 **The code:**

```python
order_total = 12.50
is_member = True
big_order = order_total > 10     # a NAMED question

print(is_member and big_order)   # both must be True
print(is_member or big_order)    # either one will do
print(not is_member)             # flips it
```

📺 **Expected output:**

```text
True
True
False
```

⚠️ **Common mistake:** Cramming everything into one enormous line of brackets. It runs, but nobody — including you next week — can read it. Naming the questions costs one line and saves an hour.

✅ **Verify:** `True`, `True`, `False`.

🎤 **Try it yourself (30 seconds):** Set `is_member = False` and rerun. The `and` line turns False, the `or` line stays True. Make sure you can say *why* out loud.

> 📌 **You saw this in class** — the same "give the question a name" idea, with numbers:
>
> ```python
> x = 14
> y = 42
> x_divisible = (x % 2 == 0)
> y_divisible = (y % 3 == 0)
> print(not (x_divisible and y_divisible))
> ```
>
> ```text
> False
> ```
>
> Both jars hold `True`, so `True and True` is `True`, and `not True` is `False`. Compare that to reading `not((x%2==0) and (y%3==0))` cold. Names win.

---

### 🧠 Quick Quiz #4 — answer from memory, before peeking

**Q1.** What is `2 + 3 * 5`?

- A) `17`
- B) `25`
- C) `10`
- D) `30`

**Q2.** What is `(7 > 3) and (2 > 5)`?

- A) `True`
- B) `False`
- C) `7`
- D) an error

**Q3.** What is `not True`?

- A) `False`
- B) `True`
- C) `None`
- D) an error

---

## ☕ Cluster E — Signboards & Receipts

*Script for this cluster:* **`scripts/05_signboards.py`**

Your shop needs words: a sign in the window, a chalkboard of specials, a receipt for every customer. All of it is text, and text has its own small toolkit.

---

### STEP 14 — Sticking letters together

▶ *In your script:* Section 1 of `scripts/05_signboards.py`

🎯 **Objective:** Join text with `+` and repeat it with `*`.

☕ **Story moment:** Your window sign uses those plastic letters that slot into a rail. To make a greeting you push words together — and if you push them too close, they touch.

🧠 **The idea in plain English:** With text, `+` glues pieces together (this is called **concatenation**) and `*` repeats. Python glues *exactly* what you give it — **it will not add a space for you**. If you want a gap, you have to supply one.

💻 **The code:**

```python
greeting = "Hello"
name = "Sara"

print(greeting + name)
print(greeting + " " + name)   # the " " is the space
print(3 * name)                # happy birthday, Sara!
```

📺 **Expected output:**

```text
HelloSara
Hello Sara
SaraSaraSara
```

⚠️ **Common mistake:** The missing space — `HelloSara` on a real customer's receipt. Look at that first line: nothing is broken, nothing errors, it just looks careless. Nobody warns you but the customer.

✅ **Verify:** Three lines: squashed, spaced, then tripled.

🎤 **Try it yourself (30 seconds):** Change `3 * name` to `5 * name`. Then try `3 * (name + " ")` and see what changes about the spacing.

> 📌 **You saw this in class:** `greeting + " " + 3*name`, giving `Hello DebelaDebelaDebela`. Same two tools.

---

### STEP 15 — Tools that come attached to text

▶ *In your script:* Section 2 of `scripts/05_signboards.py`

🎯 **Objective:** Use `.upper()`, `.lower()` and `.replace()`.

☕ **Story moment:** The sale sign needs SHOUTING. The chalkboard has a typo in it. Both are five-second jobs, because text arrives with its own little toolkit attached.

🧠 **The idea in plain English:** A **method** is a tool attached to a value, used by writing a dot after it. `.upper()` gives back a SHOUTING copy, `.lower()` a quiet copy, `.replace(old, new)` a copy with something swapped. Important: they hand back a **new** piece of text — the original is untouched.

💻 **The code:**

```python
sign = "grand opening"

print(sign.upper())
print(sign.lower())
print("Hello".replace("e", "3"))
```

📺 **Expected output:**

```text
GRAND OPENING
grand opening
H3llo
```

⚠️ **Common mistake:** Expecting `sign.upper()` to change `sign` itself. It does not. If you want to keep the shouting version, catch it in a jar: `loud_sign = sign.upper()`.

✅ **Verify:** SHOUTED, quiet, and `H3llo`.

🎤 **Try it yourself (30 seconds):** Fix a typo — take `"Wellcome"` and `.replace("ll", "l")` it.

> 📌 **You saw this in class:** `.upper()`, `.lower()`, and `greeting.replace("e", "3")` producing `H3llo`. Identical.

---

### STEP 16 — The multi-line chalkboard

▶ *In your script:* Section 3 of `scripts/05_signboards.py`

🎯 **Objective:** Write text that spans several lines.

☕ **Story moment:** Today's specials go on the big chalkboard by the door, three lines of it, laid out neatly. You want Python to keep your layout exactly as you typed it.

🧠 **The idea in plain English:** Three quote marks in a row open a piece of text that can run over as many lines as you like. Every line break and every space is kept exactly as typed.

💻 **The code:**

```python
chalkboard = """Today's specials:
  Pumpkin latte   $4.25
  Cinnamon bun    $2.75"""

print(chalkboard)
```

📺 **Expected output:**

```text
Today's specials:
  Pumpkin latte   $4.25
  Cinnamon bun    $2.75
```

⚠️ **Common mistake:** Using single quotes for multi-line text. `"Today's specials:` on one line breaks immediately — a normal quoted string must start and end on the same line. **Three quotes, or one line. Pick one.**

✅ **Verify:** Three lines, indented exactly as written in the code.

🎤 **Try it yourself (30 seconds):** Add a third special to the chalkboard. Keep the spacing lined up — you will see the layout is entirely yours to control.

---

### STEP 17 — Receipts with real numbers in them

▶ *In your script:* Section 4 of `scripts/05_signboards.py`

🎯 **Objective:** Put values inside text with f-strings, `.format()` and comma-`print`.

☕ **Story moment:** Every receipt is the same sentence with different numbers dropped in. Rather than gluing fragments together with `+`, you want a template with gaps — and the numbers just slot in.

🧠 **The idea in plain English:** An **f-string** is the modern way. Put `f` before the opening quote, then any jar name in `{curly brackets}` gets swapped for its value. Two older ways still worth recognising: `.format()`, and simply separating things with commas inside `print()` (which adds spaces for you).

💻 **The code:**

```python
cups = 18
total = cups * 3.50

print(f"We sold {cups} cups for ${total}")
print("Welcome to {}!".format("The Cozy Bean"))
print("We sold", cups, "cups")
print("The menu has " + str(76) + " items")
```

📺 **Expected output:**

```text
We sold 18 cups for $63.0
Welcome to The Cozy Bean!
We sold 18 cups
The menu has 76 items
```

⚠️ **Common mistake:** Forgetting the `f`. Without it, `"We sold {cups} cups"` prints the curly brackets *literally* — `We sold {cups} cups`. If you see braces in your output, you forgot the `f`.

✅ **Verify:** Four lines. The `$63.0` is correct but looks a little unfinished for money — the bonus below fixes exactly that.

🎤 **Try it yourself (30 seconds):** Add a line: `print(f"Tomorrow we hope for {cups + 10} cups")`. Yes — you can do maths *inside* the curly brackets.

> 📌 **You saw this in class:** gluing text to a number directly fails —
>
> ```python
> print("The menu has " + 76 + " items")
> ```
>
> ```text
> TypeError: can only concatenate str (not "int") to str
> ```
>
> **Translated:** *"`+` on text needs text on both sides."* The fix is `str(76)`, exactly as in the code above. An f-string sidesteps the whole problem, which is why everyone prefers them now.

> ### 🚀 Bonus — beyond class: making money look like money
>
> `$63.0` on a receipt looks unfinished. Adding `:.2f` inside the curly brackets means *"show exactly two digits after the point"*:
>
> ```python
> total = 63.0
> print(f"Total: ${total:.2f}")
> ```
>
> ```text
> Total: $63.00
> ```
>
> Nothing else in this lab depends on this — it is here because it takes five seconds and makes your work look real.

---

### STEP 18 — Why scripts need `print()`, and what `#` is for

▶ *In your script:* Section 5 of `scripts/05_signboards.py`

🎯 **Objective:** Understand why scripts stay silent, and how to leave notes.

☕ **Story moment:** After hours, the shop is dark. Anything you want to know, you have to switch a light on for. A script is the same: it will happily do a hundred calculations and tell you about **none** of them unless you ask.

🧠 **The idea in plain English:** In a script, **nothing appears on screen unless you `print()` it**. (Notebooks are chattier — they show you the last thing in each cell — which is exactly why beginners get caught out when they move to scripts.) Separately, any line starting with `#` is a **comment**: a note for humans that Python ignores completely. Use comments to explain *why*, not *what*.

💻 **The code:**

```python
# This line is a note to future-you. Python skips it entirely.
print("A script only shows what you ask it to print.")
```

📺 **Expected output:**

```text
A script only shows what you ask it to print.
```

⚠️ **Common mistake:** Writing `total = cups * 3.50` and expecting to see the answer. The maths happened perfectly — you simply never asked to see it. **No `print()`, no output.**

✅ **Verify:** One line. The comment produced nothing at all, exactly as intended.

🎤 **Try it yourself (30 seconds):** Put a `#` at the start of the `print` line, save, rerun. Silence. That is how you switch a line off without deleting it — hugely useful when hunting a bug.

---

### 🧠 Quick Quiz #5 — answer from memory, before peeking

**Q1.** What does `"ha" * 3` produce?

- A) `hahaha`
- B) `ha ha ha`
- C) `ha3`
- D) an error

**Q2.** What does `print(f"Total: {2+2}")` show?

- A) `Total: {2+2}`
- B) `Total: 22`
- C) `Total: 4`
- D) an error

**Q3.** What does a `#` at the start of a line do?

- A) Makes the line run twice
- B) Makes the line print in bold
- C) Marks the line as an error
- D) Makes Python ignore the line

---

## ☕ Cluster F — The Order Queue

*Script for this cluster:* **`scripts/06_order_queue.py`**

It is 8:15 on Monday and there are four people waiting. You need a container that keeps things **in order**.

---

### STEP 19 — The queue, and the famous position zero

▶ *In your script:* Section 1 of `scripts/06_order_queue.py`

🎯 **Objective:** Create a list and read an item out of it by position.

☕ **Story moment:** Four customers, in order: Sara, Ben, Aisha, Marcus. First come, first served — the order genuinely matters. And here is the one thing that trips up every single beginner: **Python counts the front of the queue as position 0.**

🧠 **The idea in plain English:** A **list** holds several things in order, written in square brackets and separated by commas. You read an item using its **index** (its position number) in square brackets. Positions start at **0**, not 1. So the first person is `queue[0]`, the second is `queue[1]`.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

print(queue)
print(queue[0])   # the FIRST person is at position 0
```

📺 **Expected output:**

```text
['Sara', 'Ben', 'Aisha', 'Marcus']
Sara
```

⚠️ **Common mistake:** Reaching for `queue[1]` to get the first person and quietly serving the wrong customer all morning. **Zero is the front of the line.** Say it once more and it is yours forever.

✅ **Verify:** The whole list, then `Sara`. Notice Python shows the list with single quotes — that is just its house style for displaying text.

🎤 **Try it yourself (30 seconds):** Print `queue[2]`. Predict who it is *before* you run it.

> 📌 **You saw this in class** — the same idea, with fruit:
>
> ```python
> fruits = ["apple", "banana", "cherry", "date"]
> print(fruits[3])
> ```
>
> ```text
> date
> ```
>
> Four fruits, positions 0, 1, 2, 3 — so position **3** is the *fourth* one, `date`. If you expected `cherry`, you have just met the zero-counting rule the hard way, which is the best way.

---

### STEP 20 — The back of the queue, and how long it is

▶ *In your script:* Section 2 of `scripts/06_order_queue.py`

🎯 **Objective:** Use negative indexing and `len()`.

☕ **Story moment:** You glance up. Who is last? How many are waiting? You should not have to count heads every time — especially when the queue keeps changing.

🧠 **The idea in plain English:** A **negative index** counts from the back: `[-1]` is always the last item, whatever the length. And `len()` hands back how many items there are.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

print(queue[-1])    # always the last one
print(len(queue))   # how many are waiting
```

📺 **Expected output:**

```text
Marcus
4
```

⚠️ **Common mistake:** Mixing up the two counting systems. Positions from the front start at **0**; positions from the back start at **-1**. (There is no `-0` — it would be the same as `0`.) Also note: `len()` counts normally, so a 4-item list has length `4` but its last position is `3`.

✅ **Verify:** `Marcus` then `4`.

🎤 **Try it yourself (30 seconds):** Print `queue[-2]` — the second-from-last. Predict, then check.

---

### STEP 21 — Serving a slice of the queue

▶ *In your script:* Section 3 of `scripts/06_order_queue.py`

🎯 **Objective:** Take a section out of a list with slicing.

☕ **Story moment:** Your new part-timer offers to take the next couple of customers. You do not want the whole queue — just customers two and three.

🧠 **The idea in plain English:** **Slicing** takes a run of items: `queue[1:3]` means *"start at position 1, stop **before** position 3."* The start is included, the end is not. Yes, that feels odd at first. The upside: the numbers subtract neatly — `3 - 1 = 2` items.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

print(queue[1:3])
```

📺 **Expected output:**

```text
['Ben', 'Aisha']
```

⚠️ **Common mistake:** Expecting `Marcus` to be included. `[1:3]` stops **before** 3, so position 3 is left out. Want him too? Use `[1:4]`.

✅ **Verify:** A two-item list containing Ben and Aisha.

🎤 **Try it yourself (30 seconds):** Try `queue[0:2]`, then `queue[2:4]`. Between them they cover the whole queue — a neat way to prove the rule to yourself.

---

### STEP 22 — Joining and leaving the queue

▶ *In your script:* Section 4 of `scripts/06_order_queue.py`

🎯 **Objective:** Add with `.append()` and remove with `.remove()`.

☕ **Story moment:** Priya walks in and joins the back. A moment later Ben's phone rings, he apologises, and leaves. Queues change constantly — that is their whole nature.

🧠 **The idea in plain English:** `.append(thing)` adds to the **end** of the list. `.remove(thing)` deletes the **first matching item by name** — you say *who*, not *where*. Both change the list itself, right where it stands.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

queue.append("Priya")   # joins the back
print(queue)

queue.remove("Ben")     # cancels and leaves
print(queue)
```

📺 **Expected output:**

```text
['Sara', 'Ben', 'Aisha', 'Marcus', 'Priya']
['Sara', 'Aisha', 'Marcus', 'Priya']
```

⚠️ **Common mistake:** Writing `queue = queue.append("Priya")`. These methods change the list *and* hand back nothing — so that line quietly replaces your whole queue with nothing at all. **Just call it on its own line.**

✅ **Verify:** Five names, then four with Ben gone.

🎤 **Try it yourself (30 seconds):** Append your own name, then remove `"Marcus"`. Print after each step so you can watch it happen.

---

### STEP 23 — Pre-numbered queue tickets

▶ *In your script:* Section 5 of `scripts/06_order_queue.py`

🎯 **Objective:** Generate a run of numbers with `range()`.

☕ **Story moment:** You buy one of those little ticket dispensers. Rather than writing 0, 1, 2, 3, 4 by hand, you ask for a run of five tickets.

🧠 **The idea in plain English:** `range(5)` produces the numbers **0, 1, 2, 3, 4** — it starts at 0 and stops **before** 5 (the same "stop before" rule as slicing). Python keeps a range tucked away efficiently rather than building the whole list, so wrap it in `list()` when you want to *see* it.

💻 **The code:**

```python
print(list(range(5)))
```

📺 **Expected output:**

```text
[0, 1, 2, 3, 4]
```

⚠️ **Common mistake:** Expecting `range(5)` to include 5. It does not — five numbers, starting at zero, ending at four. And `print(range(5))` without `list()` shows you `range(0, 5)`, which is Python describing the ticket machine rather than printing the tickets.

✅ **Verify:** `[0, 1, 2, 3, 4]`.

🎤 **Try it yourself (30 seconds):** Try `list(range(3))` and `list(range(10))`. In Lab02 this becomes genuinely powerful, when loops arrive.

---

### STEP 24 — Mixed boxes, and the whiteboard rule

▶ *In your script:* Section 6 of `scripts/06_order_queue.py`

🎯 **Objective:** See that lists hold mixed types, and understand **mutability**.

☕ **Story moment:** The lost-and-found box holds an umbrella, three odd gloves, half a sandwich and a very optimistic lottery ticket. Nothing matches. The box does not mind. And your order queue? It is a **whiteboard** — you wipe a name off and write a new one, all day long.

🧠 **The idea in plain English:** A list can hold different types at once. More importantly: lists are **mutable**, meaning they *can be changed after they are made*. You can overwrite any position directly.

> **The one picture to remember:**
> **Mutable = a whiteboard.** Wipe it, rewrite it, same board. *(Lists are whiteboards.)*
> **Immutable = ink on printed paper.** To change it you must print a fresh one. *(Text and tuples are ink.)*

💻 **The code:**

```python
lost_and_found = ["umbrella", 3, 4.5, True]   # all sorts, all fine
print(lost_and_found)

queue = ["Sara", "Aisha", "Marcus", "Priya"]
queue[0] = "Dev"       # wipe position 0, write a new name
print(queue)
```

📺 **Expected output:**

```text
['umbrella', 3, 4.5, True]
['Dev', 'Aisha', 'Marcus', 'Priya']
```

⚠️ **Common mistake:** Assuming everything works this way. It does not — in STEP 25 you will try the identical move on a tuple and get an error. That contrast is the whole point of mutability.

✅ **Verify:** The mixed box, then the queue with `Dev` where `Sara` was.

🎤 **Try it yourself (30 seconds):** Change `queue[2]` to your own name. Print before and after.

> ### 🚀 Bonus — beyond class: three more list tricks
>
> None of the core lab depends on these. They are just genuinely useful.
>
> **1. Asking for a seat that does not exist.** Our fruit list has positions 0–3. Ask for position 10 *(commented out in your script — uncomment it to see it live, then comment it back)*:
>
> ```python
> fruits = ["apple", "banana", "cherry", "date"]
> print(fruits[10])
> ```
>
> ```text
> Traceback (most recent call last):
>   File "your_file.py", line 2, in <module>
>     print(fruits[10])
>           ~~~~~~^^^^
> IndexError: list index out of range
> ```
>
> **Translated:** *"You asked for position 10, and this list does not go that far."* Now you have met three error types and can tell them apart.
>
> **2. Is someone in the queue?** `in` reads exactly like English:
>
> ```python
> queue = ["Dev", "Aisha", "Marcus", "Priya"]
> print("Aisha" in queue)
> print("Ben" in queue)
> ```
>
> ```text
> True
> False
> ```
>
> **3. Tidying and counting:**
>
> ```python
> names = ["Ben", "Aisha", "Sara"]
> names.sort()
> print(names)
> print(queue.count("Dev"))
> ```
>
> ```text
> ['Aisha', 'Ben', 'Sara']
> 1
> ```
>
> `.sort()` rearranges the list in place (alphabetically for text); `.count()` says how many times something appears.

---

### 🧠 Quick Quiz #6 — answer from memory, before peeking

**Q1.** Given `fruits = ["apple", "banana", "cherry", "date"]`, what does `fruits[3]` return?

- A) `"cherry"`
- B) `"banana"`
- C) `"date"`
- D) an `IndexError`

**Q2.** Are lists mutable?

- A) Yes, they can be changed after they are created
- B) No, they are fixed once they are created

**Q3.** After `fruits.append("elderberry")`, what does `len(fruits)` return?

- A) `3`
- B) `4`
- C) `5`
- D) `6`

---

## ☕ Cluster G — Menus & Members

*Script for this cluster:* **`scripts/07_menus_members.py`**

Three more containers, each solving a problem a list cannot.

---

### STEP 25 — The printed receipt (tuples)

▶ *In your script:* Section 1 of `scripts/07_menus_members.py`

🎯 **Objective:** Use a tuple, and see what happens when you try to change one.

☕ **Story moment:** The receipt slides out of the printer: one latte, $3.50, served by Sara. It is a record of something that *happened*. If a customer could take a pen and change the price on their copy, receipts would be worthless. Some things need to be un-editable — that is not a limitation, it is the point.

🧠 **The idea in plain English:** A **tuple** is a list that cannot be changed — **immutable**. Round brackets instead of square ones. You read it exactly like a list. You simply cannot rewrite it.

💻 **The code:**

```python
receipt = ("latte", 3.50, "Sara")

print(receipt)
print(receipt[0])   # reading works just like a list
```

📺 **Expected output:**

```text
('latte', 3.5, 'Sara')
latte
```

⚠️ **Common mistake:** Treating it like a whiteboard. Try to rewrite a tuple and Python stops you:

```python
colors = ("red", "green", "blue")
colors[0] = "yellow"
```

```text
Traceback (most recent call last):
  File "your_file.py", line 2, in <module>
    colors[0] = "yellow"
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

**Translated:** *"This is a tuple. You cannot assign a new value into one of its positions."* Compare that with STEP 24, where the very same move on a list worked perfectly. **Same syntax, different container, different rules** — that is mutability in one picture.

✅ **Verify:** The tuple prints with round brackets, and `latte` on its own. Note `3.50` displays as `3.5` — same value, tidier display.

🎤 **Try it yourself (30 seconds):** In the script, uncomment the `colors` lines and run it to meet the error yourself. Then comment them back.

> 📌 **You saw this in class:** this exact demo — `colors[0] = "yellow"` on a tuple of `("red", "green", "blue")`.

---

### STEP 26 — The menu on the wall (dictionaries)

▶ *In your script:* Section 2 of `scripts/07_menus_members.py`

🎯 **Objective:** Create a dictionary and look things up by name.

☕ **Story moment:** A customer asks what a latte costs. You do not think *"latte is the first item on the menu, so position 0"* — you just look up **latte** and read the price beside it. That is a fundamentally different way of finding things than a queue position.

🧠 **The idea in plain English:** A **dictionary** stores pairs: a **key** and its **value**. Curly brackets, and each pair written `key: value`. You look things up by key, never by position. In your shop, the key is a drink name and the value is its price.

💻 **The code:**

```python
menu = {"latte": 3.50, "espresso": 2.75, "muffin": 2.25}

print(menu)
print(menu["latte"])   # look up by NAME, not position
```

📺 **Expected output:**

```text
{'latte': 3.5, 'espresso': 2.75, 'muffin': 2.25}
3.5
```

⚠️ **Common mistake:** Trying `menu[0]`. There is no position 0 in a dictionary — asking for one gives a `KeyError`, meaning *"I have no key called 0."* Keys are names here, and each one must be unique: two entries called `"latte"` cannot coexist, exactly like a real menu.

✅ **Verify:** The full menu, then `3.5`.

🎤 **Try it yourself (30 seconds):** Look up `menu["muffin"]`. Then try `menu["tea"]` — which you do not sell — and read the `KeyError`. Errors are teachers.

---

### STEP 27 — Changing the menu

▶ *In your script:* Section 3 of `scripts/07_menus_members.py`

🎯 **Objective:** Add and change entries; list the keys and values.

☕ **Story moment:** Autumn arrives, so the pumpkin latte goes up on the board. And with bean prices rising, the muffin has to go up by 25c. Menus change — they are whiteboards, not receipts.

🧠 **The idea in plain English:** Assign to a key and Python does the sensible thing: **if the key is new it gets added; if it already exists its value is replaced.** `.keys()` hands back just the names, `.values()` just the prices.

💻 **The code:**

```python
menu = {"latte": 3.50, "espresso": 2.75, "muffin": 2.25}

menu["pumpkin latte"] = 4.25   # brand-new item
menu["muffin"] = 2.50          # existing item, new price

print(menu)
print(menu.keys())
print(menu.values())
```

📺 **Expected output:**

```text
{'latte': 3.5, 'espresso': 2.75, 'muffin': 2.5, 'pumpkin latte': 4.25}
dict_keys(['latte', 'espresso', 'muffin', 'pumpkin latte'])
dict_values([3.5, 2.75, 2.5, 4.25])
```

⚠️ **Common mistake:** Expecting a warning when you overwrite. There is none — the muffin's old price is simply gone. Adding and replacing look identical; only the key decides which happens.

✅ **Verify:** Four items, muffin now `2.5`, pumpkin latte on the end. The `dict_keys([...])` wrapper is just Python labelling what kind of view it is handing you.

🎤 **Try it yourself (30 seconds):** Add your own favourite drink at your own price, then print `menu.keys()` again to see it appear.

---

### STEP 28 — The member list (sets)

▶ *In your script:* Section 4 of `scripts/07_menus_members.py`

🎯 **Objective:** Use a set to hold only unique items.

☕ **Story moment:** The loyalty scheme launches and the clipboard fills up. Sara signs up in the morning, forgets, and signs again after lunch. She is enthusiastic. She is still **one member**.

🧠 **The idea in plain English:** A **set** is a collection that automatically refuses duplicates. Curly brackets like a dictionary, but plain items with no `key: value` pairs. Feed a list into `set()` and every duplicate silently vanishes. One trade-off: a set does **not** keep things in order, so you cannot index it — order is precisely what it gives up in exchange for uniqueness.

💻 **The code:**

```python
sign_ups = {1, 2, 3, 4, 5, 5}   # note the two 5s
print(sign_ups)

todays_sign_ups = ["Sara", "Ben", "Sara", "Aisha"]
unique_members = set(todays_sign_ups)
print(len(unique_members))
```

📺 **Expected output:**

```text
{1, 2, 3, 4, 5}
3
```

⚠️ **Common mistake:** Expecting a set to stay in the order you typed. It will not, and it has no positions — `unique_members[0]` is an error. If order matters to you, you want a list.

✅ **Verify:** Only one `5` survives, and four sign-ups collapse to `3` distinct members.

🎤 **Try it yourself (30 seconds):** Add `"Ben"` to `todays_sign_ups` again and rerun. The signature count would rise, but `len(unique_members)` stays at `3`. That is the whole superpower.

> 📌 **You saw this in class:** `{1, 2, 3, 4, 5, 5}` printing as `{1, 2, 3, 4, 5}`. The duplicate simply never makes it in.

---

### 🧠 Quick Quiz #7 — answer from memory, before peeking

**Q1.** `colors = ("red", "green", "blue")`. What does `colors[0] = "yellow"` raise?

- A) a `NameError`
- B) a `TypeError`
- C) a `ValueError`
- D) an `IndexError`

**Q2.** How many items are in `{1, 2, 3, 4, 5, 5}`?

- A) `4`
- B) `5`
- C) `6`
- D) `7`

**Q3.** How do you get the price of `"latte"` out of the `menu` dictionary?

- A) `menu[0]`
- B) `menu["latte"]`
- C) `menu("latte")`
- D) `menu.latte()`

---

> ## 🚀 Bonus — beyond class: take a real order
>
> *Script:* **`scripts/08_bonus_take_an_order.py`**
>
> Nothing in this lab depends on this. It is here because it is the most fun twenty seconds you will spend today: `input()` lets the program ask *you* a question and use your answer.
>
> ```python
> name = input("What's your name? ")
> drink = input("What can I get you? ")
> print(f"Thanks {name}! One {drink} coming right up.")
> ```
>
> Run it with `python scripts/08_bonus_take_an_order.py`. Here is a run where the answers typed were `Sara` and `Flat white`:
>
> ```text
> What's your name? What can I get you? Thanks Sara! One Flat white coming right up.
> That's $3.50 please.
> Enjoy your flat white, SARA!
> ```
>
> *(Both questions appear on one line in this transcript because the answers were piped in rather than typed. When you run it yourself, each question waits on its own line.)*
>
> ⚠️ **The program STOPS and waits for you to type. That blinking cursor is your turn, not a freeze.** Type an answer, press Enter. Whatever `input()` hands back is always text (`str`) — so `input()` for a price needs `float()` before you can do maths with it.

---

## 5. 🏋️ Practice Problems

Now the real learning starts. Reading code feels easy; writing it is where it sticks. Expect this part to be harder than the walkthrough — **that difficulty is the point**, not a sign you missed something.

**How practice works here:**

- One problem per file, in `practice/`. Run just the one you are working on: `python practice/p01_price_tags.py`
- Every file's header repeats the task **and the exact output you are aiming for**, so you can check yourself without asking anyone.
- Each file runs as-is before you touch it — it just prints the wrong things. Your job is to fill in the `TODO` lines.
- Answers live in `solutions/`, one matching file each. **Open a solution only after a real attempt.** Reading the answer first feels efficient and teaches almost nothing.
- Stuck for more than ten minutes? Reread the matching STEP, then peek. Getting unstuck is also a skill.

| # | File | Story task | You will practise |
|---|---|---|---|
| p01 | `p01_price_tags.py` | Put the shop name, cup count and price on the shelf; print each with its type. | variables, types, `type()` |
| p02 | `p02_supplier_labels.py` | The invoice arrives as text — repackage it and work out the restock cost. | casting, `str()` |
| p03 | `p03_till_math.py` | Ring up 3 lattes and 2 muffins; leftovers with `%`; the promo with `**`; precedence. | arithmetic |
| p04 | `p04_free_cookie_rule.py` | Work out who gets a free cookie, using named questions. | comparisons, `and`/`or`/`not` |
| p05 | `p05_signboard.py` | Build the sale sign, fix a typo, put up the chalkboard, print a receipt line. | strings, methods, f-strings |
| p06 | `p06_order_queue.py` | Run the morning queue: who is first, who is last, serve one, add one, slice. | lists |
| p07 | `p07_menu_and_members.py` | Look up prices, add a seasonal drink, count members without duplicates. | dicts, sets, tuples |
| 🚀 p08 | `p08_bonus_your_own_order.py` | **Bonus:** type in a real order and print a receipt for it. | `input()`, `:.2f` |

> 🚀 **p08 is a bonus** and uses `input()`, which was not in your class session. Nothing else depends on it. Skip it guilt-free — or do it, because it is the most fun file in the lab.

---

## 6. 📚 Cheat Sheet & Glossary

Two reference files ship with this lab. Lessons fade; reference sheets get used for years.

- **[CHEATSHEET.md](CHEATSHEET.md)** — every piece of syntax from this lab on one page, each with a tiny example. Print it and keep it by your laptop.
- **[GLOSSARY.md](GLOSSARY.md)** — every technical word from this lab, explained in one plain sentence. When a word stops making sense, it is here.

---

## 7. 🤔 Reflection (2 minutes — please actually do this)

Writing answers down, even briefly, roughly doubles what you will remember next week. Three questions:

1. **What clicked?** Which idea made you think *"oh — that's all it is"*?
2. **What is still fuzzy?** Name the one thing you would ask about if an instructor were sitting beside you. (Write it down — it is your first question at the next session.)
3. **Where do you already do this?** Find one labeled jar, one queue, or one menu in your own life. What would you name it in `snake_case`?

---

## 8. ✅ Answer Key

*No peeking until you have answered. Twenty questions in total.*

### Quiz #1

| Q | Answer | Why |
|---|---|---|
| 1 | **D** — shows the words on the screen | `print()` displays; it does not store or send anything anywhere. |
| 2 | **C** — `648.56402` | Without quotes, Python works the sum out before showing it. |

### Quiz #2

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — `25` | A jar holds one thing; refilling replaces the contents rather than adding to them. |
| 2 | **D** — `<class 'float'>` | The decimal point makes it a `float`. |
| 3 | **C** — a `NameError` | Names are case-sensitive, so `Cups_Sold` is a jar that was never created. |

### Quiz #3

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — `int("forty-two")` | `int()` needs text that really looks like a number; words raise a `ValueError`. |
| 2 | **B** — a `TypeError` | Python refuses to add a number to text rather than guess what you meant. |
| 3 | **D** — the text `"42"` | `str()` converts a number into text, so it can be glued into sentences. |

### Quiz #4

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — `17` | Multiplication happens before addition: `3*5` is 15, plus 2. |
| 2 | **B** — `False` | `and` needs both sides True, and `2 > 5` is False. |
| 3 | **A** — `False` | `not` flips `True` into `False`. |

### Quiz #5

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — `hahaha` | `*` repeats text with nothing added between the copies. |
| 2 | **C** — `Total: 4` | An f-string works out whatever is inside the curly brackets. |
| 3 | **D** — makes Python ignore the line | `#` marks a comment: a note for humans only. |

### Quiz #6

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — `"date"` | Counting starts at 0, so positions are 0,1,2,3 and position 3 is the *fourth* item. Not an error — the list has four items. |
| 2 | **A** — yes, they can be changed | Lists are mutable: the whiteboard you can wipe and rewrite. |
| 3 | **C** — `5` | It started with four items and `.append()` added a fifth. |

### Quiz #7

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — a `TypeError` | A tuple is immutable, so it does not support item assignment. |
| 2 | **B** — `5` | Sets refuse duplicates, so the second `5` never makes it in. |
| 3 | **B** — `menu["latte"]` | Dictionaries are looked up by key in square brackets, never by position. |

---

## 9. ➡️ What's Next

**Lab02 — The Cozy Bean Gets Busy.** Three weeks on, there is a queue out of the door and you have hired Sara, Ben and Aisha as baristas.

You will stop making every decision yourself and start writing **rules** the shop follows without you (`if` / `elif` / `else`), **loops** that serve an entire queue without you writing a line per customer, and **recipe cards** (functions) you write once and use forever. Then you will give the shop a memory: a real order notebook it can write to and read back the next morning.

Everything you built today — jars, types, the till, queues, the menu — is the foundation Lab02 stands on. See you at the shop. ☕

> 📥 **Lab02 is a separate repo.** Look for its GitHub Classroom link in Google Classroom, then clone it into `AperionAI/Module1/Week1/Lab02` — right next to this one:
>
> ```text
> cd ~/AperionAI/Module1/Week1
> git clone PASTE-YOUR-LAB02-REPO-URL-HERE Lab02
> ```
>
> (Windows PowerShell: `cd ~\AperionAI\Module1\Week1` — same `git clone` line.) Keeping both folders side by side is what makes the links between the two labs' cheat sheets work.

---

*Aperion AI Training Academy · Module 1: AI/ML Fundamentals · Week 1 · Lab01*
*"Boundless Possibilities, Infinite Potential"*

