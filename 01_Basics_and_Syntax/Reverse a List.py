"""
Script to accept a list of integers from the user and print the list in reverse order.
"""

li = [int(x) for x in input().split()]
li.reverse()
print(li)