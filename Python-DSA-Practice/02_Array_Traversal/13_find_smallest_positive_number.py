''' Finding the smallest positive number'''
arr = [-8, 4, -10, 7, 2, -5]
smallest=0
found=False
for num in arr:
    if num>0:
        if found==False:
            smallest=num
            found=True
        if found:
            if num<smallest:
                if num>0:
                    smallest=num
if found:
    print(smallest)
else:
    print("no positive number")