n = int(input())
a = list(map(int, input().split()))

node_max = [1]
for i in range(1, n+1):
    node_max.append(min(10**18, node_max[i-1]*2-a[i]))

a.reverse()
node_max.reverse()

node_max2 = [a[0]]
node_min2 = [a[0]]

for i in range(n):
    node_max2.append(node_max2[-1]+a[i+1])
    node_min2.append((node_min2[-1]+1)//2+a[i+1])

if node_min2[-1] != 1:
    print(-1)
else:
    ans = 0
    for i in range(n+1):
        ans += min(node_max[i]+a[i], node_max2[i])

    print(ans)
