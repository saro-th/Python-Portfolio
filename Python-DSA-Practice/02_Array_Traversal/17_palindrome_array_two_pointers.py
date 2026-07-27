'''Palindrome'''
arr = [1, 2, 3, 2, 1]
found=True
left=0
right=len(arr)-1
while(left<right):
 if arr[left]!=arr[right]:
        found=False
        break
 else:
    
     
     left+=1
     right-=1
if found:
    print("palindrom")
else:
    print("not palindrome")

  

    


