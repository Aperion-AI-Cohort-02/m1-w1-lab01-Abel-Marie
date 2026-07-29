# ============================================================
#  SOLUTION p07 -- The Menu and the Members
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p07_menu_and_members.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


menu = {"latte": 3.50, "espresso": 2.75, "muffin": 2.25}

print("Latte costs:", menu["latte"])
print("Espresso costs:", menu["espresso"])

menu["hot chocolate"] = 3.25   # a brand-new key appears
menu["muffin"] = 2.50          # an existing key gets a new price

print("Menu now:", menu)
print("Drinks we sell:", menu.keys())

sign_up_sheet = ["Sara", "Ben", "Sara", "Aisha", "Ben"]

print("Signatures collected:", len(sign_up_sheet))
print("Different members:", len(set(sign_up_sheet)))

# A printed receipt is a tuple -- set in ink, cannot be changed.
receipt = ("latte", 3.50, "Sara")
print("Receipt drink:", receipt[0])
