# ============================================================
#  PRACTICE p08 -- 🚀 BONUS -- Take Your Own Order
#  The Cozy Bean  |  M1-W1 Lab01
#
#  🚀 Bonus -- beyond class. This one uses input(), which was
#  not in your session. Nothing else in this lab depends on it.
#  Skip it with a clear conscience, or enjoy it -- it is fun.
#
#  YOUR TASK:
#    Ask a real customer (you!) for a name and a drink, then
#    print a friendly receipt showing the price with two
#    decimal places, the way real money is written.
#
#  AN EXAMPLE RUN (yours will say whatever you type):
#    What's your name? Sara
#    What can I get you? Latte
#    --- THE COZY BEAN ---
#    Thanks Sara! One latte coming up.
#    Total: $3.50
#
#  NOTE: when you run this, the program STOPS and waits for
#  you. That blinking cursor is your turn, not a freeze. Type
#  an answer and press Enter.
#
#  HINT: whatever input() hands back is always text (str).
#
#  How to run it: python practice/p08_bonus_your_own_order.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? See solutions/p08_bonus_your_own_order.py.
# ============================================================


# TODO 1: ask for the customer's name with input()
name = "Sara"

# TODO 2: ask what drink they would like
drink = "Latte"

price = 3.50

print("--- THE COZY BEAN ---")

# TODO 3: greet them by name, with the drink in lower case
print("Thanks ...! One ... coming up.")

# TODO 4: print the total with 2 decimal places, using {price:.2f}
print("Total: $...")
