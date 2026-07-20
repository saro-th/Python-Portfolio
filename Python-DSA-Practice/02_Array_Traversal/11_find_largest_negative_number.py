''' Find the largest negative number'''
arr = [8, -4, 10, -7, -2, 5]
largest=0
found=False
for num in arr:
    if num<0:
      if  found==False:
          largest=num
          found=True
    if found:
        if num>largest:
            if num<0:
             largest=num
if found:
    print(largest)
else:
    print("no negative number")