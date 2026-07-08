"""
Script to remove duplicate elements from a list using a secondary list, maintaining order.
"""

li = [int(x) for x in input().split()]
lis = []
for i in li:
    if i not in lis:
        lis.append(i)
print(lis)