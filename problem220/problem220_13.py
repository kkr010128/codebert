S,T=map(str,input().split())
a,b=map(int,input().split())
U=input()
if U == S:
  a +=-1
elif U == T:
  b += -1
print(a,b)