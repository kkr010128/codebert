A, B, M = map(int, input().split())

price_A = list(map(int, input().split()))
price_B = list(map(int, input().split()))
min_A = min(price_A)
min_B = min(price_B)

ans = min_A + min_B
for i in range(M):
    x, y, c = map(int, input().split())
    ans = min(price_A[x-1]+price_B[y-1]-c,ans)

print(ans)
