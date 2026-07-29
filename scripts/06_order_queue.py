# ============================================================
#  The Cozy Bean -- Script 06: The Order Queue
#  Lab STEPs 19-24, plus 3 bonus bits at the end.
#  Shows: lists -- the line of customers waiting. Counting
#         from 0, slicing, adding and removing.
#  Run:   python scripts/06_order_queue.py  (from M1-W1-Lab01/)
# ============================================================

# ---- Section 1  (STEP 19): the queue, and position 0 -------
# A list keeps several things in order, inside square brackets.
queue = ["Sara", "Ben", "Aisha", "Marcus"]
print(queue)
print(queue[0])   # the FIRST person is at position 0, not 1!

# 📌 You saw this in class -- the same idea with fruit:
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[3])

# ---- Section 2  (STEP 20): the back of the line, and size --
print(queue[-1])   # -1 means "last", counting from the back
print(len(queue))  # len() counts how many are waiting

# ---- Section 3  (STEP 21): serving a slice of the queue ----
print(queue[1:3])  # from position 1, stop BEFORE position 3

# ---- Section 4  (STEP 22): joining and leaving the queue ---
queue.append("Priya")   # a new customer joins the back
print(queue)
queue.remove("Ben")     # Ben cancels and leaves
print(queue)

# ---- Section 5  (STEP 23): pre-numbered queue tickets ------
print(list(range(5)))   # range() builds 0,1,2,3,4

# ---- Section 6  (STEP 24): mixed types, and mutability -----
# A list can hold different kinds of things (the lost-and-found).
lost_and_found = ["umbrella", 3, 4.5, True]
print(lost_and_found)

# Lists are MUTABLE: you can wipe an entry and write a new one.
queue[0] = "Dev"
print(queue)

# ---- 🚀 Bonus -- beyond class: a seat that isn't there
#   print(fruits[10])
# IndexError: list index out of range

# ---- 🚀 Bonus -- beyond class: is that person in the queue?
print("Aisha" in queue)   # she is still waiting
print("Ben" in queue)     # he cancelled back in Section 4

# ---- 🚀 Bonus -- beyond class: tidy up and count
names = ["Ben", "Aisha", "Sara"]
names.sort()               # alphabetical order, in place
print(names)
print(queue.count("Dev"))  # how many times does Dev appear?
