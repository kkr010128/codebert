a,b,c=map(int,input().split())
if a>c:
    print(a-c,b)
elif a<=c and b<=(c-a):
    print(0,0)
else:
    print(0,b-(c-a))