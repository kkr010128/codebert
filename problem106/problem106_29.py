n = int(input())
cnt = [0] * 11000

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            value = x*x + y*y + z*z + x*y + y*z + z*x
            if value <= n:
                cnt[value] += 1

for i in range(1,n+1):
    print(cnt[i])
