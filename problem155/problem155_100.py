n, m = map(int, input().split())
H = list(map(int, input().split()))
check = [1]*n

for _ in range(m):
    a, b = map(int, input().split())
    if H[a-1] >= H[b-1]:
        check[b-1] = 0
    if H[a-1] <= H[b-1]:
        check[a-1] = 0

print(sum(check))