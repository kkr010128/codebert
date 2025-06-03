N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

ba = []
for i, j in ab:
    ba.append([j, i])

ab.sort()
ba.sort(reverse = True)

if N % 2 == 1:
    n = (N+1) // 2 - 1
    ans = ba[n][0] - ab[n][0] + 1
    
else:
    n = N // 2 - 1
    ans = (ba[n][0] + ba[n+1][0]) - (ab[n][0] + ab[n+1][0]) + 1

print(ans)