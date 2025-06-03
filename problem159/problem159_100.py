N = int(input())
i = 100
cnt = 0
while True:
    i += i // 100
    cnt += 1
    if i >= N:
        print(cnt)
        exit()