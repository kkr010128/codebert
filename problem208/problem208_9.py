n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(m)]

if n==1 and all([i[1]==0 for i in li]):
    print(0)
    exit()
for i in range(10**(n-1),10**n):
    p = list(map(int,list(str(i))))
    for s,c in li:
        if p[s-1] != c:break
    else:
        print(i)
        exit()
print(-1)