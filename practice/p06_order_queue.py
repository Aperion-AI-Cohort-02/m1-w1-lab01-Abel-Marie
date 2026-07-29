# ============================================================
#  PRACTICE p06 -- The Morning Queue
#  The Cozy Bean  |  M1-W1 Lab01
#
#  YOUR TASK:
#    Five people are waiting. Print who is first, who is last,
#    and how many are waiting. Then serve Sara (she leaves the
#    queue), let Dev join the back, and print the queue after
#    each change. Finish by printing the next two people to
#    serve, using a slice.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    First in line: Sara
#    Last in line: Priya
#    People waiting: 5
#    After serving Sara: ['Ben', 'Aisha', 'Marcus', 'Priya']
#    After Dev joins: ['Ben', 'Aisha', 'Marcus', 'Priya', 'Dev']
#    Next two to serve: ['Aisha', 'Marcus']
#
#  HINT: the first person is at position 0, and [-1] is always
#        the last one, however long the queue gets.
#
#  How to run it: python practice/p06_order_queue.py
#                 (run it from inside the M1-W1-Lab01 folder)
#
#  Stuck? The answer is in solutions/p06_order_queue.py -- but
#  give it a real try first. The struggle makes it stick.
# ============================================================


queue = ["Sara", "Ben", "Aisha", "Marcus", "Priya"]

# TODO 1: print the FIRST person (remember: position 0)
print("First in line:", queue)

# TODO 2: print the LAST person
print("Last in line:", queue)

# TODO 3: print how many people are waiting
print("People waiting:", 0)

# TODO 4: Sara has been served -- take her out of the queue
print("After serving Sara:", queue)

# TODO 5: Dev joins the back of the queue
print("After Dev joins:", queue)

# TODO 6: print the next two people to serve, using a slice.
#         (careful -- Ben is being served right now, so it is
#          the two AFTER him that we want)
print("Next two to serve:", queue)
