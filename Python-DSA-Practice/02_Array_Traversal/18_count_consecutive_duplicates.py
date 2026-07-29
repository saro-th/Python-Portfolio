''' Counting  consecutive duplicates'''
arr=[1,1,2,2,2,3,4,4]
count=1
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        count+=1
        
    else:
        if count>1:
            
            print(arr[i],"times",count)
        count=1

if arr[i]==arr[i+1]:
    
    print(arr[i+1],"times",count)
else:
    print("no consecutive duplicates")   
        
              