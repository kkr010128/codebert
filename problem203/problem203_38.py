A,B = map(int, input().split())

#0.10%を基準にする
k_min = B * 10
k_max = (B+1) * 10

ans = -1
for k in range(k_min, k_max):
    if k * 8 // 100 == A:
        ans = k
        break
print(ans)