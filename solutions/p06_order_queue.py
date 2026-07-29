# ============================================================
#  SOLUTION p06 -- The Morning Queue
#  The Cozy Bean  |  M1-W1 Lab01
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p06_order_queue.py
#                 (run it from inside the M1-W1-Lab01 folder)
# ============================================================


queue = ["Sara", "Ben", "Aisha", "Marcus", "Priya"]

print("First in line:", queue[0])    # position 0, not 1!
print("Last in line:", queue[-1])    # -1 counts from the back
print("People waiting:", len(queue))

queue.remove("Sara")
print("After serving Sara:", queue)

queue.append("Dev")
print("After Dev joins:", queue)

# Ben (position 0) is at the counter now, so the next two are
# positions 1 and 2. A slice stops BEFORE the second number.
print("Next two to serve:", queue[1:3])
