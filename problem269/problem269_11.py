t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1 = t1*(a1-b1)
c2 = t2*(a2-b2)
d = c1 + c2
if d == 0:
  print("infinity")
elif c1*c2 > 0 or c1*d > 0:
  print(0)
else:
  if abs(c1)%abs(d)==0:
    print((abs(c1)//abs(d))*2)
  else:
    print((abs(c1)//abs(d))*2+1)