'''
Array Traversal – Find the Smallest Element'''
arr = [12, 18, 7, 25, 15]
smallest=arr[0]

for num in arr:
    if num<smallest:
        smallest=num
print(smallest)