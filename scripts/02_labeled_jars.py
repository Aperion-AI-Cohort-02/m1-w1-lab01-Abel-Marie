# ============================================================
#  The Cozy Bean  --  Script 02: Labeled Jars
#
#  What this shows : variables (labeled jars), reusing them in
#                    maths, capital letters, and the 4 data types.
#  Lab STEPs       : STEP 3, 4, 5 and 6
#  How to run it   : python scripts/02_labeled_jars.py
#                    (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# ---- Section 1  (STEP 3): your first labeled jar -----------
# Put the number 12 into a jar labeled beans_in_stock.
beans_in_stock = 12
print(beans_in_stock)

# The afternoon delivery arrives. We refill the SAME jar --
# a jar holds one thing, so this REPLACES the 12. It is not 62.
beans_in_stock = 50
print(beans_in_stock)


# ---- Section 2  (STEP 4): let the jars do the maths --------
cups_sold = 18
price = 3.50

# A brand-new jar, filled with maths done on the other two.
money_today = cups_sold * price
print(money_today)
print(cups_sold + 4)   # 4 free cups for the builders next door

# 📌 You saw this in class: the London <-> Edinburgh trip,
# this time stored in jars instead of typed as raw numbers.
distance_to_london_miles = 403
mile_to_km = 1.60934
distance_london_edinburgh_km = distance_to_london_miles * mile_to_km
print(distance_london_edinburgh_km)


# ---- Section 3  (STEP 5): capital letters make new jars ----
Cups_Sold = 99         # a DIFFERENT jar -- the capitals matter!
print(cups_sold)
print(Cups_Sold)

# In class this jar was written as marathonMiles. Python allows
# that, but our house style is snake_case: all lowercase words
# joined by underscores.
marathon_miles = 26.2
marathon_km = marathon_miles * mile_to_km
print("Marathon distance in km:", marathon_km)


# ---- Section 4  (STEP 6): four kinds of jars ---------------
shop_name = "The Cozy Bean"   # str  -- text, always in quotes
is_open = True                # bool -- only True or False

print(type(cups_sold))        # int   -- a whole number
print(type(price))            # float -- has a decimal point
print(type(shop_name))
print(type(is_open))
