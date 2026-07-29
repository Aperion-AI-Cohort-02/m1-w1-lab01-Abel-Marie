# ============================================================
#  The Cozy Bean  --  Script 04: The Till
#
#  What this shows : arithmetic, order of precedence, comparison
#                    questions, and combining rules with and/or/not.
#  Lab STEPs       : STEP 10, 11, 12 and 13
#  How to run it   : python scripts/04_the_till.py
#                    (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# ---- Section 1  (STEP 10): the four everyday operators -----
a = 10
b = 5

print(a + b)   # add
print(a - b)   # subtract
print(a * b)   # multiply
print(a / b)   # divide -- division ALWAYS gives a decimal


# ---- Section 2  (STEP 11): leftovers, powers, precedence ---
muffins_baked = 26
print(muffins_baked % 12)   # % = the remainder, boxed by the dozen
print(2 ** 3)               # ** = a "double double double"

# 📌 You saw this in class: the till multiplies BEFORE it adds.
print(2 + 3 * 5)     # 3*5 happens first
print((2 + 3) * 5)   # brackets go first, so 2+3 happens first


# ---- Section 3  (STEP 12): questions with yes/no answers ---
# A comparison always answers True or False -- never a number.
order_total = 12.50

print(order_total > 10)       # is it a big order?
print(order_total < 10)       # is it a small order?
print(order_total == 10)      # == asks "are these equal?"
print(order_total != 10)      # != asks "are these different?"
print(order_total >= 12.50)   # at least this much?
print(order_total <= 12.50)   # at most this much?


# ---- Section 4  (STEP 13): combining rules at the counter --
# Free cookie if they are a member AND the order is over $10.
is_member = True
big_order = order_total > 10

print(is_member and big_order)   # both must be True
print(is_member or big_order)    # either one will do
print(not is_member)             # not flips True and False

# 📌 You saw this in class: giving a question a NAME makes the
# rule readable. Compare this to one long line of brackets.
x = 14
y = 42
x_divisible = (x % 2 == 0)
y_divisible = (y % 3 == 0)
print(not (x_divisible and y_divisible))
