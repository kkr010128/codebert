n,k = map(int, input().split())
L = [i for i in range(1,n+1)]
for _ in range(k):
    d = int(input())
    a = sorted(list(map(int, input().split())))
    for e in a:
        if e in L:
            L.remove(e)
print(len(L))