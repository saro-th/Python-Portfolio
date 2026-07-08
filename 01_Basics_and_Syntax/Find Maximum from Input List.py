"""
Script to find and print the maximum value from a user-inputted list of integers.
"""

thing = [int(y) for y in input().split()]
maximum = thing[0]
for i in thing:
    if i > maximum:
        maximum = i
print(maximum)