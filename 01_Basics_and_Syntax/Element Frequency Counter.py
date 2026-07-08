"""
Script to count how many times a specific target number appears in a user-inputted list.
"""

li = [int(u) for u in input().split()]
target = int(input("which number"))
count = 0
for i in li:
    if target == i:
        count += 1

print("target", target)
print("count", count)
