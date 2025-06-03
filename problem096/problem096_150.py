n, d = list(map(int, input().split(' ')))
res = 0

for _ in range(n):
    x, y = list(map(int, input().split(' ')))
    if d ** 2 >= (x ** 2) + (y ** 2):
        res += 1

print(res)