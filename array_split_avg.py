n=int(input(''))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
print(a)
m=a[:len(a)//2]
n=a[len(a)//2:]
avg1=sum(m)/len(m)
avg2=sum(n)/len(n)
if(avg1==avg2):
  print("Yes")
else:
  print('No')
