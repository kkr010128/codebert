from math import ceil

n = int(input())
a = list(map(int, input().split()))

a.reverse()

max_tree = [0] * (n+1)
min_tree = [0] * (n+1)

max_tree[0] = a[0]
min_tree[0] = a[0]
for i in range(1, n+1):
    max_tree[i] = max_tree[i-1] + a[i]
    min_tree[i] = ceil(min_tree[i-1]/2) + a[i]

max_tree.reverse()
min_tree.reverse()

if min_tree[0] > 1:
    print(-1)
    exit()

a.reverse()
possible = [0] * (n+1)
possible[0] = 1

for i in range(1, n+1):
    possible[i] = min((possible[i-1]-a[i-1])*2, max_tree[i])

print(sum(possible))
