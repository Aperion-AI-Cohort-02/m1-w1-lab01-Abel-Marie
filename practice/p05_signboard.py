# ============================================================
#  PRACTICE p05 -- The Signboard
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    Make the shop's signs. SHOUT "grand opening". Chant the
#    word Cozy three times with spaces between. Fix the typo in
#    "Wellcome to The Cozy Bean". Put up a multi-line chalkboard
#    of today's specials. Finish with a receipt line built from
#    an f-string: Sara ordered 2 lattes at 3.50 each.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    GRAND OPENING
#    Cozy Cozy Cozy
#    Welcome to The Cozy Bean
#    Today's specials:
#      Latte    $3.50
#      Muffin   $2.25
#    Sara ordered 2 lattes for 7.0 dollars
#
#  HINT: three quotes in a row let a piece of text run over
#        several lines, exactly as you type it.
#
#  How to run it: python practice/p05_signboard.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p05_signboard.py -- but
#  give it a real try first. The struggle makes it stick.
# ============================================================


sign = "grand opening"

# TODO 1: print the sign in capital letters
print(sign)

# TODO 2: print "Cozy Cozy Cozy" -- careful, no space on the end!
#         (tip: 2 * "Cozy " gives you "Cozy Cozy ")
print("Cozy")

# TODO 3: fix the double L in Wellcome using .replace()
greeting = "Wellcome to The Cozy Bean"
print(greeting)

# TODO 4: make this chalkboard run over three lines by using
#         triple quotes instead of the single quotes below
chalkboard = "Today's specials:"
print(chalkboard)

# TODO 5: finish the receipt line with an f-string so it uses
#         the two jars below instead of hard-coded numbers
cups = 2
total = cups * 3.50
print("Sara ordered ? lattes for ? dollars")
