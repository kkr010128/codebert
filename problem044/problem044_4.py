a,b,c = [int(i) for i in input().split()]
res = 0
for num in range(a,b+1):
    if c%num == 0:
        res += 1
print(res)