a=list(input(''))
b=list(input(''))
arr=[]
for i in range(0,len(a)):
  if (a[i]==b[i]):
    arr.append(a[i])
  else:
    break
print(''.join(str(x) for x in arr))
  
