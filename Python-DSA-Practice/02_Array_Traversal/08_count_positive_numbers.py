''' Array Traversal – Count Positive Numbers'''
arr = [-5, 8, -2, 10, 0, 7, -1]
count=0
for num in arr:
    if num>0:
        count+=1
print(count)