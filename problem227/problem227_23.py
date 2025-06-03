n,k = map(int,input().split())
h = [int(s) for s in input().split()]
h.sort(key=int)
for _ in range(min(k,len(h))):del h[-1]
print(sum(h))