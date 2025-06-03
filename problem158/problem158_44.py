a=int(input())
b,c=map(int,input().split())
x=(b//a)*a
if b<=x<=c:
  print("OK")
elif b<=x+a<=c:
  print("OK")
else:
  print("NG")