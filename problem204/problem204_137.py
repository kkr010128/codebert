S = input()
Q = int(input())
b = "" #reversed
a = ""
f = 0
for i in range(Q):
  q = input()
  if q == "1":
    f+=1
  else:
    _,F,C = q.split()
    if (f+int(F))%2==1:
      b+=C
    else:
      a+=C
if f%2==0:
  print(b[::-1]+S+a)
else:
  print(a[::-1]+S[::-1]+b)