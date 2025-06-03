n = int(input())
arms = []
for _ in range(n):
    x, l = map(int, input().split())
    arms.append((x - l, x + l))
arms.sort(key = lambda x : x[1])

last_right = arms[0][1]
ans = 1
for i in range(1, n):
    left, right = arms[i]
    if left < last_right:
        continue
    last_right = right
    ans += 1

print(ans)