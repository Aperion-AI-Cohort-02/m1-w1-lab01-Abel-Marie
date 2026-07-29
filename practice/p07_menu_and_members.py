# ============================================================
#  PRACTICE p07 -- The Menu and the Members
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    Look up two prices on the menu. Add a seasonal drink,
#    "hot chocolate" at 3.25, and put the muffin price up to
#    2.50. Print the whole menu and then just the drink names.
#    Today's sign-up sheet has some people on it twice -- print
#    how many signatures there were, and how many DIFFERENT
#    people that is. Finish by reading the drink off a printed
#    receipt.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Latte costs: 3.5
#    Espresso costs: 2.75
#    Menu now: {'latte': 3.5, 'espresso': 2.75, 'muffin': 2.5, 'hot chocolate': 3.25}
#    Drinks we sell: dict_keys(['latte', 'espresso', 'muffin', 'hot chocolate'])
#    Signatures collected: 5
#    Different members: 3
#    Receipt drink: latte
#
#  HINT: a set quietly throws duplicates away, so len() of a
#        set counts how many DIFFERENT things there were.
#
#  How to run it: python practice/p07_menu_and_members.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p07_menu_and_members.py --
#  but give it a real try first. The struggle makes it stick.
# ============================================================


menu = {"latte": 3.50, "espresso": 2.75, "muffin": 2.25}

# TODO 1: look up the two prices BY NAME (not by position!)
print("Latte costs:", 0)
print("Espresso costs:", 0)

# TODO 2: add "hot chocolate" at 3.25 to the menu

# TODO 3: change the muffin price to 2.50

print("Menu now:", menu)

# TODO 4: print just the drink names
print("Drinks we sell:", menu)

sign_up_sheet = ["Sara", "Ben", "Sara", "Aisha", "Ben"]

# TODO 5: how many signatures, and how many different people?
print("Signatures collected:", 0)
print("Different members:", 0)

# A printed receipt is a tuple -- set in ink, cannot be changed.
receipt = ("latte", 3.50, "Sara")

# TODO 6: print just the drink from the receipt
print("Receipt drink:", receipt)
