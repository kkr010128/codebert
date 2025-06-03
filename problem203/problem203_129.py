a, b = map(int, input().split())
cnt = 0
for i in range(1101):
    if (i*8)//100 == a and(i*10)//100 == b:
        print(i)
        break
    else:
        cnt += 1
        if cnt == 1101:
            print(-1)
            break