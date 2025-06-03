k = int(input())
ans = 1
seven = 7
for i in range(k):
    if seven % k == 0:
        print(ans)
        exit()
    seven = (seven * 10 + 7) % k
    ans += 1
print(-1)