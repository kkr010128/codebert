tmp = input().split()
a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])
k = int(tmp[3])
if(a>=k):
  print(k)
elif(a+b>=k):
  print(a)
else:
  print(a-(k-a-b))