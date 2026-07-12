'''
Array Traversal – Find the Largest Even Number'''
arr = [39, 12, 5, 18, 9, 20, 3]
largest=0
found=False
for num in arr:
  if num%2==0:
      found=True
  if found==True:
      if num>largest:
         largest=num
  
if found:  
   print(largest)
else:
    print("no even")
     
    