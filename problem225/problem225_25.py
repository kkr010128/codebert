h,a=map(int,input().split())
s=h//a
t=h%a
if t==0:
    print(s)
else:
    print(s+1)