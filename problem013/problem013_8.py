n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

min_v = r[0]
max_p = -1000000000
for i in range(1,n):
    max_p = max(max_p,r[i]-min_v)
    min_v = min(min_v,r[i])
print(max_p)