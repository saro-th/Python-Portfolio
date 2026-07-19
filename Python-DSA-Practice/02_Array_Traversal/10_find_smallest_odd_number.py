''' Finding the the smallest odd number'''
arr = [8, 5, 10, 3, 6, 7]
smallest=0
found=False
for num in arr:
     if num%2!=0:
      if found==False:
      
          smallest=num
          found=True
     if found:    
      if num<smallest:
          if num%2!=0:
               smallest=num
               
if found:
     print(smallest)
else:
     print("no odd")