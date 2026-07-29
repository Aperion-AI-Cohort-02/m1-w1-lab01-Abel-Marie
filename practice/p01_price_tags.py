# ============================================================
#  PRACTICE p01 -- Price Tags
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    It is opening morning. Put three things on your shelf:
#    the shop's name, how many cups you sold today (18), and
#    what one cup costs (3.50). Print them, then ask Python
#    what KIND of thing is in each jar.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Shop name: The Cozy Bean
#    Cups sold: 18
#    Price per cup: 3.5
#    Type of shop_name: <class 'str'>
#    Type of cups_sold: <class 'int'>
#    Type of price_per_cup: <class 'float'>
#
#  HINT: type() reads the fine print on a jar and tells you
#        what kind of thing is inside.
#
#  How to run it: python practice/p01_price_tags.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p01_price_tags.py -- but
#  give it a real try first. The struggle is what makes it stick.
# ============================================================


# TODO 1: put the shop's name into this jar (it is text!)
shop_name = ""

# TODO 2: put today's cup count into this jar (a whole number)
cups_sold = 0

# TODO 3: put the price of one cup into this jar (it has cents)
price_per_cup = 0

print("Shop name:", shop_name)
print("Cups sold:", cups_sold)
print("Price per cup:", price_per_cup)

# TODO 4: print the TYPE of each jar, using type()
#         The first one is done for you -- copy the pattern.
print("Type of shop_name:", type(shop_name))
