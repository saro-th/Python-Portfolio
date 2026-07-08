"""
Script to find and print characters that appear exactly once in a user-inputted string.
"""

word = input()

for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    if count == 1:
        print(i)