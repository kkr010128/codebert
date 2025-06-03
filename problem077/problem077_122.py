a, b, c, d = [int(i) for i in input().split()]

res = float("-inf")

for i in [a,b]:
    for j in [c,d]:
        res = max(i * j, res)
        
print(res)