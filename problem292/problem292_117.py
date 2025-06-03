N = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(N-1):
        if i == j:
            break
        else:
            ans = ans + d[i]*d[j]
print(ans)
