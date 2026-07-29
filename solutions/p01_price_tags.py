# ============================================================
#  SOLUTION p01 -- Price Tags
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p01_price_tags.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


shop_name = "The Cozy Bean"   # str   -- text, always in quotes
cups_sold = 18                # int   -- a whole number
price_per_cup = 3.50          # float -- it has a decimal point

print("Shop name:", shop_name)
print("Cups sold:", cups_sold)
print("Price per cup:", price_per_cup)

print("Type of shop_name:", type(shop_name))
print("Type of cups_sold:", type(cups_sold))
print("Type of price_per_cup:", type(price_per_cup))

# Notice that 3.50 prints as 3.5 -- Python never shows a
# trailing zero it does not need. The value is exactly the same.
