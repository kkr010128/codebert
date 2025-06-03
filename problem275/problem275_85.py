x = list(map(int, input().split()))
ans = 0
for i in x:
    if i == 1:
        ans += 300000
    elif i == 2:
        ans += 200000
    elif i == 3:
        ans += 100000

if ans == 600000:
    print(1000000)
else:
    print(ans)
