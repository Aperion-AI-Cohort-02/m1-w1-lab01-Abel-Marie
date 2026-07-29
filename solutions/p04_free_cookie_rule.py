# ============================================================
#  SOLUTION p04 -- The Free Cookie Rule
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p04_free_cookie_rule.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


# ---- Sara ----
sara_is_member = True
sara_order = 12.50

# Giving the question a NAME is what makes the rule readable.
sara_big_order = sara_order > 10
sara_gets_cookie = sara_is_member and sara_big_order

print("Sara is a member:", sara_is_member)
print("Sara has a big order:", sara_big_order)
print("Sara gets a free cookie:", sara_gets_cookie)

# ---- Ben ----
ben_is_member = False
ben_order = 7.00

ben_big_order = ben_order > 10
ben_gets_cookie = ben_is_member and ben_big_order

print("Ben is a member:", ben_is_member)
print("Ben has a big order:", ben_big_order)
print("Ben gets a free cookie:", ben_gets_cookie)

# not flips True into False, and False into True.
ben_invite = not ben_is_member
print("Ben should be invited to sign up:", ben_invite)
