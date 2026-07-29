# ============================================================
#  PRACTICE p02 -- The Supplier's Paper Labels
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    The bean supplier's invoice arrives as TEXT: 12 bags at
#    3.50 each, both written on a paper label. Repackage them
#    into real numbers, work out the restock cost, then write
#    one sentence about it by turning the number back to text.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Bags ordered: 12
#    Price per bag: 3.5
#    Restock cost: 42.0
#    Note for the file: we spent 42.0 dollars on beans today
#
#  HINT: int() and float() turn text into numbers you can do
#        maths with. str() turns a number back into text.
#
#  How to run it: python practice/p02_supplier_labels.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p02_supplier_labels.py --
#  but give it a real try first. The struggle makes it stick.
# ============================================================


# This is exactly how it arrives from the supplier: as TEXT.
bags_label = "12"
price_label = "3.50"

# TODO 1: repackage bags_label into a whole number
bags = 0

# TODO 2: repackage price_label into a decimal number
price_per_bag = 0

print("Bags ordered:", bags)
print("Price per bag:", price_per_bag)

# TODO 3: work out the restock cost (bags times price per bag)
restock_cost = 0

print("Restock cost:", restock_cost)

# TODO 4: finish this line so the number becomes part of the
#         sentence. Gluing text with + needs text on both sides!
print("Note for the file: we spent " + "???" + " dollars on beans today")
