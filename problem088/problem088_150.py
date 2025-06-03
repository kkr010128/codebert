n = int(input())
vals = list(map(int, input().split()))

ma = vals[0]
res = [0 for _ in range(n)]
for i, val in enumerate(vals):
    if val < ma: 
        res[i] = ma - val
    if ma < val:
        ma = val

print(sum(res))