N = int(input())
A = list(map(int, input().split()))
t = [(i + 1, A[i]) for i in range(N)]
t_sorted = sorted(t, key=lambda a: a[1])
ans = ''
for i in range(N):
    ans += str(t_sorted[i][0]) + ' '
print(ans)
