N = int(input())
a = list(map(int,input().split()))

aset = set(a)
if 1 not in aset:
    print(-1)
else:
    nex = 1
    counter = 0
    for i in range(N):
        if a[i] == nex:
            nex += 1
        else:
            counter += 1
    print(counter)