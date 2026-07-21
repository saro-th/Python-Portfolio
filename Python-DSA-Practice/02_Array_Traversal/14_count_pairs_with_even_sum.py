''' Counting the even sum'''
arr = [2, 3, 4, 5]
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j])%2==0:
            count+=1
print(count)            