# ============================================================
#  SOLUTION p08 -- 🚀 BONUS -- Take Your Own Order
#  The Cozy Bean  |  M1-W1 Lab01
#
#  🚀 Bonus -- beyond class.
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  AN EXAMPLE RUN (yours will say whatever you type):
#    What's your name? Sara
#    What can I get you? Latte
#    --- THE COZY BEAN ---
#    Thanks Sara! One latte coming up.
#    Total: $3.50
#
#  How to run it: python solutions/p08_bonus_your_own_order.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# input() shows the question, waits for you, and hands back
# whatever you typed -- always as text.
name = input("What's your name? ")
drink = input("What can I get you? ")

price = 3.50

print("--- THE COZY BEAN ---")
print(f"Thanks {name}! One {drink.lower()} coming up.")

# :.2f means "show exactly 2 numbers after the dot" -- so 3.5
# is written the way money is written: 3.50
print(f"Total: ${price:.2f}")
