N = int(input())
A = list(map(int, input().split()))

max_list = []
m = 0
ans = 0
for a in A:
    ans += max(m - a, 0)
    max_list.append(m)
    m = max(m, a)

print(ans)