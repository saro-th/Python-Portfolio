"""
Script to accept a list of integers and filter out only the odd numbers into a new list.
"""

num = [int(x) for x in input().split()]
li = []
for i in num:
    if i % 2 != 0:
        li.append(i)
print(li)