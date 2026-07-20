''' Finding the greater than average  count '''
arr = [10, 20, 30, 40, 50]
count=0
element=0
average=0
total=0
for num in arr:
  total+=num
  element+=1
average=total/element
for num in arr:
    
    if num>average:
        count+=1
print(count)
