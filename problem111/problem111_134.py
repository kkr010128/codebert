N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = A[0]
cnt = 1
for a in A[1:]:
    if cnt + 1 < N:
        ans += a
        cnt += 1

    if cnt+ 1 < N:
        ans += a
        cnt += 1
print(ans)
