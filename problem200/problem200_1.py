A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[min(a)+min(b)]
for i in range(M):
    a1,b1,c1 =map(int,input().split())
    d=a[a1-1]+b[b1-1]-c1
    c.append(d)
print(min(c))
