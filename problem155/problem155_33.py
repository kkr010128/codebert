n,m = map(int,input().split())
h = list(map(int,input().split()))
h.insert(0,0)
good = [0] + [1] * n
for i in range(m):
    x,y = map(int,input().split())
    if h[x] > h[y]:
        good[y] = 0
    elif h[x] < h[y]:
        good[x] = 0
    else:
        good[x] = 0
        good[y] = 0

print(sum(good))
