# ☕ M1-W1-Lab01 — Opening Week at The Cozy Bean

**Aperion AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 1 |
| **Lab** | Lab01 — Opening Week at The Cozy Bean |
| **Topic** | Python basics: variables, data types, casting, operators, strings, lists, tuples, dictionaries, sets |
| **Duration** | **≈ 1 hour** of lab work (one-time setup not counted) |
| **Difficulty** | ⭐ Absolute Beginner — no experience assumed, none at all |

You have just opened a coffee shop, and you are going to teach Python how it works. Everything in this lab has a physical twin behind your counter: a variable is a labeled jar, a list is the customer queue, a dictionary is the menu on the wall.

**Start here → [`M1-W1-Lab01.md`](M1-W1-Lab01.md)** — that is the full lab, 28 steps with a story, code, expected output and quizzes.

> 🎁 **This repo is self-contained.** Every file you need is already here. You never create a file in this lab — you only *open*, *edit*, *save* and *run* files.

---

## 1. 📥 Get this repo onto your computer

You reached this repo by clicking the **GitHub Classroom link posted in Google Classroom**. That link made **your own private copy** of the lab — the URL has your GitHub username in it, and nobody else can see your work in it. This is the copy you clone.

### 1.1 Where to put it

Please use this folder layout on your computer. Every lab in the course gets its own folder, so nothing ever collides and you can always find last week's work:

```text
AperionAI/
└── Module1/
    ├── Week1/
    │   ├── Lab01/      ← this repo
    │   └── Lab02/      ← next repo
    ├── Week2/
    │   ├── Lab01/
    │   └── Lab02/
    └── Week3/
        ├── Lab01/
        └── Lab02/
```

Put `AperionAI` somewhere you will find it again — your home folder, Documents, or Desktop. **Do not put it inside OneDrive, iCloud Drive, Google Drive or Dropbox.** Those services sync files while Python is using them and cause errors that look like bugs in your code but are not.

### 1.2 Copy your repo's address

1. On this repo's page on GitHub, click the green **`Accept Assignment`** button.
2. Make sure the **HTTPS** tab is selected.
3. Click the 📋 copy icon next to the address.

You now have something like `https://github.com/AperionAI-2026/M1-W1-Lab01-<your-username>.git` on your clipboard. **That address is yours** — the `<your-username>` part is what makes it yours, so use your own and not a classmate's.

### 1.3 Clone it into `Week1/Lab01`

Open a terminal — on Windows, **PowerShell**; on Mac, **Terminal** — and run these lines one at a time. Replace `PASTE-YOUR-REPO-URL-HERE` with what you just copied (right-click pastes in PowerShell; **Cmd+V** on Mac).

**Windows (PowerShell):**

```text
cd ~
mkdir -Force AperionAI\Module1\Week1
cd AperionAI\Module1\Week1
git clone PASTE-YOUR-REPO-URL-HERE Lab01
cd Lab01
```

**Mac / Linux:**

```text
cd ~
mkdir -p AperionAI/Module1/Week1
cd AperionAI/Module1/Week1
git clone PASTE-YOUR-REPO-URL-HERE Lab01
cd Lab01
```

That last word — `Lab01` — matters. Without it, git would name the folder after the repo (`M1-W1-Lab01-your-username`), which is long, has your username buried in it, and does not match the rest of the course. Adding `Lab01` tells git what to call the folder.

> **`git` is not recognised?** Install it from [git-scm.com/downloads](https://git-scm.com/downloads), accept every default, then **close and reopen your terminal** and try again.
>
> **Would rather not use git at all?** On the repo page click **`< > Code` → Download ZIP**, then unzip it and rename the unzipped folder to `Lab01`, placed at `AperionAI/Module1/Week1/Lab01`. Everything in the lab works exactly the same. You just cannot push your work back this way.

### 1.4 Check you landed in the right place

```text
pwd
ls
```

`pwd` should end in **`Week1/Lab01`** (Windows shows it with backslashes: `...\Week1\Lab01`). `ls` should show `README.md`, `M1-W1-Lab01.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `scripts`, `practice` and `solutions`.

---

## 2. 🔧 Set up Python and VS Code

If this is your first lab, do these three things once and then never again. The lab document walks through each in detail — this is the short version.

**① Do you have Python?**

```text
python --version
```

You want **3.10 or higher**. Nothing happens, or "not recognized"? On Windows try `py --version`; on Mac try `python3 --version`. If it is genuinely missing, install from [python.org/downloads](https://www.python.org/downloads/) and — on the very first installer screen — **tick "Add python.exe to PATH"**. That one tick prevents the most common beginner setup problem in the world.

**② Get VS Code.** It is a free text editor; think Microsoft Word for code. [code.visualstudio.com](https://code.visualstudio.com/)

**③ Open this lab in VS Code.**

1. Open VS Code → **File → Open Folder…**
2. Choose your **`Lab01`** folder — the one you just cloned.
3. **Terminal → New Terminal.** A panel opens along the bottom, already standing inside `Lab01`, which is exactly where every command in this lab must be run from.

**Now run your first program:**

```text
python scripts/01_opening_day.py
```

```text
Hello World
Welcome to The Cozy Bean!
10.5
12.75
648.56402
```

If you see that, you are ready. Open [`M1-W1-Lab01.md`](M1-W1-Lab01.md) and begin.

> 💡 **Read the lab document inside VS Code:** open `M1-W1-Lab01.md`, then press **Ctrl+Shift+V** (Mac: **Cmd+Shift+V**) for a nicely formatted preview you can read side by side with your code.

---

## 3. 📂 What is in this repo

| Path | What it is |
|---|---|
| [`M1-W1-Lab01.md`](M1-W1-Lab01.md) | **The lab.** 28 steps, 7 clusters, 5 quizzes, answer key. Work through this. |
| [`CHEATSHEET.md`](CHEATSHEET.md) | Every command and piece of syntax from this lab on one page. Print it. |
| [`GLOSSARY.md`](GLOSSARY.md) | Plain-English definitions — shop word on the left, Python word on the right. |
| `scripts/` | Eight runnable scripts, one per cluster. Read them, run them, tweak them. |
| `practice/` | Eight practice problems. **This is where you write your own code.** |
| `solutions/` | Worked solutions to the practice problems. Try yours first — genuinely. |

Suggested rhythm: read a STEP → run the matching script in `scripts/` → do the 30-second tweak → and after each cluster, do the matching problem in `practice/`.

> 🛋️ **Aim for one sitting of about an hour.** If you do need to pause, stop after any 🧠 Quick Quiz — that is always a clean break.

---

## 4. 💾 Saving your work back to GitHub

Your edits live on your computer until you push them. Pushing keeps a backup, and it is how your instructor can see your progress if you ask for help. From inside `Lab01`:

```text
git add .
git commit -m "Finished Cluster C"
git push
```

Do that when you finish, or any time you pause. If it is your first ever push, git may ask who you are — answer once and it remembers:

```text
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Not using git (ZIP route)? Skip this section — just keep the folder safe.

---

## 5. 🆘 If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError` / `can't open file` | You are running from the wrong folder. | Type `pwd`. Does it end in `Lab01`? If not, **File → Open Folder** on `Lab01` and open a fresh terminal. |
| `'python' is not recognized…` (Windows) | Windows cannot find Python. | Try `py scripts/01_opening_day.py`. If that fails, reinstall Python with **"Add python.exe to PATH"** ticked. |
| `command not found: python` (Mac) | Mac calls it something else. | Use `python3 scripts/01_opening_day.py`. |
| `'git' is not recognized` | Git is not installed. | Install from [git-scm.com](https://git-scm.com/downloads), then reopen your terminal. |
| **Output did not change after an edit** | **The file was never saved.** | Look for the ● dot on the file tab. **Ctrl+S** / **Cmd+S**. Rerun. This is the answer nine times out of ten. |
| `SyntaxError` | A typo — usually a missing quote or bracket. | Read the line number, then look at that line **and the one above it**. |

Still stuck after a genuine try? Post in the course channel with **what you ran**, **what you expected**, and **the last line of the error**. Those three things get you an answer fast.

---

*Aperion AI Training Academy · Module 1, Week 1, Lab 01 · Next up: [Lab02 — The Cozy Bean Gets Busy](https://github.com/AperionAI-2026/M1-W1-Lab02-B02)*

> 🔗 Lab02 is a **separate repo** with its own GitHub Classroom link in Google Classroom. Clone it into `AperionAI/Module1/Week1/Lab02`, right next to this one.
