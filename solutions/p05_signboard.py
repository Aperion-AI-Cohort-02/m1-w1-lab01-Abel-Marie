# ============================================================
#  SOLUTION p05 -- The Signboard
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p05_signboard.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


sign = "grand opening"
print(sign.upper())

# 2 copies WITH a space, then one more without -- no stray
# space on the end.
print(2 * "Cozy " + "Cozy")

greeting = "Wellcome to The Cozy Bean"
print(greeting.replace("Wellcome", "Welcome"))

# Triple quotes keep the line breaks and spacing exactly as typed.
chalkboard = """Today's specials:
  Latte    $3.50
  Muffin   $2.25"""
print(chalkboard)

cups = 2
total = cups * 3.50
print(f"Sara ordered {cups} lattes for {total} dollars")
