k = int(input())
ans = 0

ai = 0
for i in range(k+2):
    ai = ((ai * 10) + 7) % k
    if ai == 0:
        ans = i + 1
        print(ans)
        exit()

ans = -1
print(ans)


