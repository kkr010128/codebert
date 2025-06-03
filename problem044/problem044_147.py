a, b, c = map(int, input().split())

cnt = 0

for num in range(a, b + 1):
    if c % num == 0:
        cnt += 1

print(cnt)
