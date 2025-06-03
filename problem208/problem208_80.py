n,m=map(int,input().split())
sc=[list(map(int,input().split())) for _ in range(m)]

for x in range(1000):
    sx=str(x)
    if n!=len(sx):
        continue

    for s,c in sc:
        if sx[s-1]!=str(c):
            break
    else:
        print(x)
        exit(0)

print(-1)