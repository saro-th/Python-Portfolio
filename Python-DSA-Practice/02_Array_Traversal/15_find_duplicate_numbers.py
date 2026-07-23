'''Finding the duplicates'''

arr = [7, 7, 7, 7, 7, 7]
printed=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            if arr[i] not in printed:
                print(arr[i])
                printed.append(arr[i])