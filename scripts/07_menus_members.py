# ============================================================
#  The Cozy Bean  --  Script 07: Menus & Members
#
#  What this shows : tuples (printed receipts), dictionaries
#                    (the menu), and sets (the member list).
#  Lab STEPs       : STEP 25, 26, 27 and 28
#  How to run it   : python scripts/07_menus_members.py
#                    (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# ---- Section 1  (STEP 25): the printed receipt (tuple) -----
# Round brackets make a tuple: a list that is set in ink.
receipt = ("latte", 3.50, "Sara")
print(receipt)
print(receipt[0])   # you read it exactly like a list

# 📌 You saw this in class. Trying to edit ink does not work.
# These lines are COMMENTED OUT so this script runs clean:
#
#   colors = ("red", "green", "blue")
#   colors[0] = "yellow"
#
# Traceback (most recent call last):
#   File "your_file.py", line 2, in <module>
#     colors[0] = "yellow"
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment


# ---- Section 2  (STEP 26): the menu (dictionary) -----------
# Curly brackets, and each item is  key: value.
# Here the key is a drink name and the value is its price.
menu = {"latte": 3.50, "espresso": 2.75, "muffin": 2.25}
print(menu)
print(menu["latte"])   # look it up by NAME, never by position


# ---- Section 3  (STEP 27): changing the menu ---------------
menu["pumpkin latte"] = 4.25   # a brand-new seasonal item
menu["muffin"] = 2.50          # prices went up, sorry
print(menu)

print(menu.keys())     # just the drink names
print(menu.values())   # just the prices


# ---- Section 4  (STEP 28): the member list (set) -----------
# 📌 From class: a set silently drops duplicates.
sign_ups = {1, 2, 3, 4, 5, 5}
print(sign_ups)

# Sara signed up twice today, but she is still one member.
todays_sign_ups = ["Sara", "Ben", "Sara", "Aisha"]
unique_members = set(todays_sign_ups)
print(len(unique_members))
