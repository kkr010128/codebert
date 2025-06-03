n,d=list(map(int,input().split()))
s=list(map(int,input().split()))
s=sorted(s)
s.reverse()
if d>=n:
    print(0)
else:
    c=0
    s=s[d:n]
    for i in s:
        c+=int(i)
    print(c)
