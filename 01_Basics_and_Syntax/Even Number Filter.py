"""
Script to accept a list of integers from the user and print only the even numbers.
"""

num = [int(n) for n in input().split()]

for i in num:
    if i % 2 == 0:
        print(i)