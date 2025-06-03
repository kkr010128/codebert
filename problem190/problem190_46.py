a=input()
c=len(a)
b=a[:(c-1)//2]
d=a[(c+3)//2-1:]
if a==a[::-1] and b==b[::-1] and d==d[::-1]:
  print("Yes")
else:
  print("No")