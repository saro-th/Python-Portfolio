'''Array Traversal – Sum of Even Numbers'''
arr = [3, 8, 10, 7, 6,5]
total=0
for num in arr:
    if num%2==0:
        total+=num
print(total)