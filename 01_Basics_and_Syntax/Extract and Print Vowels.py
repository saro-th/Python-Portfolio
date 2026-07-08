"""
Script to accept a string from the user and print each vowel found in it on a new line.
"""

str = input().lower()
for i in str:
    if i in "aeiou":
        print(i)