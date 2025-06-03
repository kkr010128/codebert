x = int(input())
cnt = 1
mod = 7

for i in range(x):
    if mod % x == 0:
        print(cnt)
        exit()
    mod = (10 * mod + 7) % x
    cnt += 1
print(-1)
