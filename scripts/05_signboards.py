# ============================================================
#  The Cozy Bean -- Script 05: Signboards & Receipts
#  Lab STEPs 14-18.
#  Shows: building text -- joining it, shouting it, fixing
#         typos, chalkboards, and receipts.
#  Run:   python scripts/05_signboards.py  (from M1-W1-Lab01/)
# ============================================================


# ---- Section 1  (STEP 14): sticking letters together -------
# + glues text together. It does NOT add a space for you.
greeting = "Hello"
name = "Sara"
print(greeting + name)
print(greeting + " " + name)
print(3 * name)   # 📌 from class: * repeats text


# ---- Section 2  (STEP 15): tools that come with text -------
# A method is a tool attached to a value; you call it with a dot.
sign = "grand opening"
print(sign.upper())    # SHOUTING sale sign
print(sign.lower())    # quiet again
print("Hello".replace("e", "3"))   # 📌 from class: fixing a typo


# ---- Section 3  (STEP 16): the multi-line chalkboard -------
# Three quotes let text run over several lines, exactly as typed.
chalkboard = """Today's specials:
  Pumpkin latte   $4.25
  Cinnamon bun    $2.75"""
print(chalkboard)


# ---- Section 4  (STEP 17): receipts with real numbers ------
cups = 18
total = cups * 3.50

# An f-string: put an f in front, then {} holds any jar you like.
print(f"We sold {cups} cups for ${total}")

# The older way, still common:
print("Welcome to {}!".format("The Cozy Bean"))

# Or just separate things with commas -- print adds the spaces.
print("We sold", cups, "cups")

# 📌 From class: "text " + 76 breaks, because 76 is not text.
#   print("The menu has " + 76 + " items")
#   TypeError: can only concatenate str (not "int") to str
print("The menu has " + str(76) + " items")

# 🚀 Bonus -- beyond class: :.2f shows money with 2 decimals.
print(f"Total: ${total:.2f}")


# ---- Section 5  (STEP 18): printing and comments -----------
# Any line starting with # is a sticky note for humans. Python
# skips it completely -- it never runs.
print("A script only shows what you ask it to print.")
