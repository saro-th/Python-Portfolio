'''
Array Traversal – Find the Largest Element'''
arr = [12, 18, 7, 25, 15]
largest=arr[0]

for num in arr:
    if num>largest:
        largest=num
print(largest)
