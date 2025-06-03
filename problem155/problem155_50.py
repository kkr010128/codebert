n, m = map(int, input().split())
h = list(map(int, input().split()))

l = [True] * n
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    #print(h[a],h[b])
    if h[a] >= h[b]:
        l[b] = False
    if h[a] <= h[b]:
        l[a] = False

#print(l)
print(l.count(True))