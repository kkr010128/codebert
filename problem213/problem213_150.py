n = int(input())
x = list(map(int, input().split()))
ret = 1000000
for p in range(1, 101):
    ret = min(ret, sum((x - p) ** 2 for x in x))
print(ret)
