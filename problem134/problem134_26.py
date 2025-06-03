n = int(input())
a = [int(x) for x in input().split()]
a.sort()
ans = 1

for i in a:
    ans *= i
    if ans > 10 ** 18:
        print(-1)
        break
else:
    print(ans)