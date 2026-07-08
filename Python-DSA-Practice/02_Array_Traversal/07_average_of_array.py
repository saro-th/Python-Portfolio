'''Array Traversal – Average of All Elements'''
arr = [10, 20, 30, 40]
Average=0
total=0
for num in arr:
    total+=num
Average=total/len(arr)
print(Average)