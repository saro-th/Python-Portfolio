"""
Script to count all non-vowel characters (including spaces/special characters) in a string.
"""

word = input().lower()
count = 0
for i in word:
    if i not in "aeiou":
         count += 1
         
print(count)