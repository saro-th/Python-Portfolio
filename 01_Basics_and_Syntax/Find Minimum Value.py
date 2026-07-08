"""
Script to find and print the minimum value from a user-inputted list of integers.
"""

li = [int(x) for x in input().split()]
mini = li[0]
for i in li:
    if mini > i:
        mini = i
print(mini)