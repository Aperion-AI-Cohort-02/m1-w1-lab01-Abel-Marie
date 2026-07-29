# ============================================================
#  The Cozy Bean  -  Script 08: 🚀 BONUS - Take a Real Order
#
#  🚀 Bonus - beyond class. Nothing else in this lab needs it.
#
#  What this shows : input() pauses the program and waits for
#                    YOU to type something, then uses it.
#  How to run it   : python scripts/08_bonus_take_an_order.py
#                    (run it from inside the M1-W1-Lab01 folder)
#
#  NOTE: when you run this, the program STOPS and waits for you.
#  That blinking cursor is not a freeze - it is your turn. Type
#  an answer and press Enter.
# ============================================================


# input() shows your question, waits, and hands back what was
# typed. Whatever comes back is ALWAYS text (str).
name = input("What's your name? ")
drink = input("What can I get you? ")

print(f"Thanks {name}! One {drink} coming right up.")

# Everything below is Lab01 material you already know.
price = 3.50
print(f"That's ${price:.2f} please.")
print(f"Enjoy your {drink.lower()}, {name.upper()}!")
