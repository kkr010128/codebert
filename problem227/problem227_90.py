n,k = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
for i in range(min(n,k)):
    h.pop()
print(sum(h))