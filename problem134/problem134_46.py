n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

if 0 in a:
    print(0)
    exit()

ans = 1

for i in a:
    ans *= i
    if ans > 10**18:
        print(-1)
        exit()

print(ans)