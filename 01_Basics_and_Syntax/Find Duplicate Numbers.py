"""
Script to identify and print numbers that appear more than once in a user-inputted list.
"""

li = [int(y) for y in input().split()]
printed = []
for i in li:
    count = 0
    for j in li:
        if i == j:
            count += 1
    if count > 1 and i not in printed:
        printed.append(i)
print(printed)