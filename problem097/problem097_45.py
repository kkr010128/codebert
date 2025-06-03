K=int(input())
x=7
c=1
visited={7}
while x%K:
    x*=10
    x+=7
    x%=K
    c+=1
    z=x%K
    if z in visited:
        print(-1)
        exit()
    visited.add(x%K)
print(c)
