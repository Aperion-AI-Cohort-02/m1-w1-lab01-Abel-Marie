# ============================================================
#  The Cozy Bean  --  Script 03: Repackaging (casting)
#
#  What this shows : turning text into numbers and back again,
#                    plus the two errors that happen when you
#                    mix them up by accident.
#  Lab STEPs       : STEP 7, 8 and 9
#  How to run it   : python scripts/03_repackaging.py
#                    (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# ---- Section 1  (STEP 7): repackaging paper labels ---------
# The supplier writes prices on a paper label, so they arrive
# as TEXT. You cannot do maths with a photograph of a number.
price_label = "3.50"
print(type(price_label))

# float() repackages that text into a real decimal number.
price = float(price_label)
print(type(price))
print(price * 2)

# int() repackages text into a whole number.
bags_label = "12"
bags = int(bags_label)
print(bags + 3)

# str() goes the other way: number -> text, for signs and receipts.
cups = 18
print("We sold " + str(cups) + " cups")

# int() on a decimal chops off the fraction (it does not round).
print(int(20.5))


# ---- Section 2  (STEP 8): the TypeError, on purpose --------
# 📌 From class. COMMENTED OUT so this script runs clean --
# uncomment the three lines to meet the error yourself:
#
#   x = 10
#   y = "20"
#   print(x + y)
#
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# The fix: repackage the text first, THEN add.
x = 10
y = "20"
print(x + int(y))


# ---- Section 3  (STEP 9): the ValueError, on purpose -------
# 📌 Also from class: int() only repackages text that really
# looks like a number. Words are not numbers.
#
#   print(int("Python is powerful."))
#
# ValueError: invalid literal for int() with base 10: 'Python is powerful.'
print(int("42"))   # this one works: the text really is a number
