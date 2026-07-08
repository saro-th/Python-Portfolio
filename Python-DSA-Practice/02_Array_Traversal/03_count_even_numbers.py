'''Array Traversal – Count Even Numbers'''
arr = [3, 8, 10, 7, 6, 5]
count=0
for num in arr:
    if num%2==0:
        count+=1
print(count)        