N, K = map(int, input().split())
h_int_list = list(map(int, input().split()))

ans = 0

for i in h_int_list:
    if K <= i:
        ans += 1

print(ans)
