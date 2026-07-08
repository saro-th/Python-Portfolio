"""
Script to isolate even numbers from a user-inputted list and calculate their squares.
"""

li = [int(u) for u in input().split()]
lis = []

for i in li:
    if i % 2 == 0:
        sq = i * i
        lis.append(sq)
print(lis)