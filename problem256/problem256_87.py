n,m=map(int,input().split(" "))
l=max(n,m)
s=min(n,m)
while s!=0:
    tmp = s
    s = l % s
    l = tmp
print(n*m // l)