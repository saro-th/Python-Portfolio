"""
Script to find and print the character that appears most frequently in a user-inputted string.
"""

word = input()

max_count = 0
max_char = ""

for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        max_char = i

print(max_char)