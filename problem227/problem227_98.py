n,k = map(int,input().split())
h = list(map(int,input().split()))
h.sort(reverse = True)
m = 0

for i in range(k,n):
    m += h[i]

print(m)