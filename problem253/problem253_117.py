n,a,b = map(int,input().split())
s = abs(a-b)
if s % 2 == 0:
    print(s // 2)
else:
    print(min(a-1,n-b)+1+((b-a-1) // 2))