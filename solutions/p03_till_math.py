# ============================================================
#  SOLUTION p03 -- Ringing Up the Till
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p03_till_math.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


latte_price = 3.50
muffin_price = 2.25

latte_line = 3 * latte_price
muffin_line = 2 * muffin_price
order_total = latte_line + muffin_line

print("Latte line:", latte_line)
print("Muffin line:", muffin_line)
print("Order total:", order_total)

# % hands back the remainder: 26 boxed by 12 leaves 2 over.
muffins_left_over = 26 % 12
print("Muffins left over:", muffins_left_over)

# ** raises to a power: 2 doubled, doubled, doubled again.
promo_cups = 2 ** 3
print("Promo cups:", promo_cups)

# Multiplication happens before addition, unless brackets say
# otherwise -- exactly like the maths you already know.
print("2 + 3 * 5 =", 2 + 3 * 5)
print("(2 + 3) * 5 =", (2 + 3) * 5)
