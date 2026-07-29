# ============================================================
#  SOLUTION p02 -- The Supplier's Paper Labels
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p02_supplier_labels.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# This is exactly how it arrives from the supplier: as TEXT.
bags_label = "12"
price_label = "3.50"

bags = int(bags_label)              # text -> whole number
price_per_bag = float(price_label)  # text -> decimal number

print("Bags ordered:", bags)
print("Price per bag:", price_per_bag)

restock_cost = bags * price_per_bag

print("Restock cost:", restock_cost)

# str() turns the number back into text so + can glue it in.
print("Note for the file: we spent " + str(restock_cost) + " dollars on beans today")
