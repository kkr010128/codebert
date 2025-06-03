K = int(input())

if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()
now = 0
count = 0
while True:
    now = (now * 10 + 7) % K
    count += 1
    if now % K == 0:
        print(count)
        exit()
