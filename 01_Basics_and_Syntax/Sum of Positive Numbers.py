"""
Script to calculate the total sum of only the positive integers in a user-inputted list.
"""

li = [int(y) for y in input().split()]
total = 0
for i in li:
     if i > 0:
          total += i
print(total)