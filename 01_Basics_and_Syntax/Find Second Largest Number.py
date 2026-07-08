"""
Script to find the second largest number in a list by removing the maximum value.
"""

li = [int(u) for u in input().split()]
lis = list(set(li))

maximum = lis[0]

for i in lis:
    if i > maximum:
        maximum = i
lis.remove(maximum)
maxi = lis[0]
for j in lis:
    if j > maxi:
        maxi = j
print(maxi)