"""
Script to count the number of vowels in a user-inputted string.
"""

word = input().lower()
count = 0
for i in word:
    if i in "aeiou":
        count += 1
print(count)