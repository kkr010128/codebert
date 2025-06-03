n = int(input())

a = list(map(int,input().split()))

cumsum_a = a.copy()

for i in range(n-1, -1, -1):
    cumsum_a[i] += cumsum_a[i+1]

ans = 0
childable_node = 1

for i in range(n + 1):
    if a[i] > childable_node:
        ans = -1
        break

    ans += childable_node

    if i < n:
        b_max1 = 2 * (childable_node - a[i])
        b_max2 = cumsum_a[i + 1]
        childable_node = min(b_max1, b_max2)

print(ans)