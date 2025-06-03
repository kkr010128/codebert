N, A, B = map(int, input().split())
dif = abs(A - B)
ans = 0

if dif % 2 == 0:
    ans = dif // 2
else:
    ans = min(A - 1, N - B) + 1 + dif // 2
print(ans)