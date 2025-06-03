n = int(input())
A = sorted(list(map(int, input().split())))[::-1]
if 0 in A:
    print(0)
    exit()

ans = 1
for a in A:
    ans *= a
    if ans > 10 **18:
        print(-1)
        exit()
print(ans)