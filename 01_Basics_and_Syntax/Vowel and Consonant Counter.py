"""
Script to count the number of vowels and alphabetic consonants in a user-inputted string.
"""

word = input().lower()
vowel = 0
consonant = 0
for i in word:
    if i in "aeiou":
        vowel += 1
    elif i.isalpha():
        consonant += 1
print("vowel", vowel)
print("consonant", consonant)