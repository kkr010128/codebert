N = int(input())
a = list(map(int, input().split()))

i = 1
ans = 0
for aa in a:

    if aa != i:
        ans += 1
    else:
        i += 1

if N == ans:
    print(-1)
else:
    print(ans)