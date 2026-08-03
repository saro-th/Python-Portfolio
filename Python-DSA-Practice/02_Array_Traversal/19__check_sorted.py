'''sorting'''
arr = [1, 2, 3, 4, 5]
found=True

for i in range(len(arr)-1):
    if  not arr[i]<arr[i+1]:
        found=False
        break
    
        
if found:
    print("sorted")
else:
    print("not sorted")
       
       
        
   
