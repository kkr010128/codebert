a,b,c,k=[int(i) for i in input().split()]

if a>=k:
  print(k)
elif a+b>=k:
  print(a)
else:
  print(a-(k-a-b))