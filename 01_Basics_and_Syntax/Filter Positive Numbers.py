"""
Script to accept a list of integers and filter out only the positive numbers into a new list.
"""

lt = [int(x) for x in input().split()]
pos = []
for i in lt:
    if i > 0:
        pos.append(i)
print(pos)