"""
Script to check if a user-inputted integer reads the same forward and backward.
"""

n = int(input())
ori = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if ori == rev:
    print("palindrome")   
else:
    print("not palindrome")