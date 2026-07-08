"""
Script to process a list of numbers: squares even numbers and leaves odd numbers unchanged.
"""

li = [int(y) for y in input().split()]

n = []
for i in li:
    if i % 2 == 0:
        square = i * i
        n.append(square) 
    else:
        odd = i
        n.append(odd)
     
print(n)