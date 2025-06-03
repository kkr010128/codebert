k = int(input())

now = 7
cnt = 1
used = [False] * k
ten = 10
while not used[now % k]:
    if now % k == 0:
        print(cnt)
        exit()
    used[now % k] = True
    now = (now + ten * 7) % k
    ten = ten * 10 % k
    cnt += 1
print(-1)
