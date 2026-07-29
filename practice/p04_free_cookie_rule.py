# ============================================================
#  PRACTICE p04 -- The Free Cookie Rule
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    The rule at the counter: you get a free cookie if you are
#    a loyalty member AND your order is over $10.
#      Sara IS a member and her order is $12.50.
#      Ben is NOT a member and his order is $7.00.
#    Work out the answers for both, using NAMED jars for each
#    question so the rule reads like English. Also work out
#    whether Ben should be invited to sign up.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Sara is a member: True
#    Sara has a big order: True
#    Sara gets a free cookie: True
#    Ben is a member: False
#    Ben has a big order: False
#    Ben gets a free cookie: False
#    Ben should be invited to sign up: True
#
#  HINT: a comparison such as  order_total > 10  hands back
#        True or False all by itself -- no if needed.
#
#  How to run it: python practice/p04_free_cookie_rule.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p04_free_cookie_rule.py --
#  but give it a real try first. The struggle makes it stick.
# ============================================================


# ---- Sara ----
sara_is_member = True
sara_order = 12.50

# TODO 1: is Sara's order over 10?
sara_big_order = False

# TODO 2: does Sara get a cookie? (member AND big order)
sara_gets_cookie = False

print("Sara is a member:", sara_is_member)
print("Sara has a big order:", sara_big_order)
print("Sara gets a free cookie:", sara_gets_cookie)

# ---- Ben ----
ben_is_member = False
ben_order = 7.00

# TODO 3: same two questions for Ben
ben_big_order = False
ben_gets_cookie = False

print("Ben is a member:", ben_is_member)
print("Ben has a big order:", ben_big_order)
print("Ben gets a free cookie:", ben_gets_cookie)

# TODO 4: Ben should be invited if he is NOT a member.
ben_invite = False
print("Ben should be invited to sign up:", ben_invite)
