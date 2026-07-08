"""
Script to accept a list of integers and calculate the sum of only the even numbers.
"""

li = [int(y) for y in input().split()]
sum = 0
for i in li:
    if i % 2 == 0:
        sum = sum + i
print(sum)