n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

maxv = -(10**9)
mina = a[0]

for i in range(1,n):
    maxv = max(maxv, a[i]-mina)
    mina = min(mina, a[i])

print(maxv)