X = int(input())

if 360 % X == 0:
    print(360 // X)
    exit()
else:
    mod = 0
    cnt = 0
    while (360 + mod) % X != 0:
        cnt += (360 + mod) // X
        mod = (360 + mod) % X
    cnt += (360 + mod) // X

print(cnt)
