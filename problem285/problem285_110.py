s = input()
n = len(s)
left = [0 for _ in range(n+1)]
right = [0 for _ in range(n+1)]

tmp = 0
for i in range(n):
    if s[i] == '<':
        tmp += 1
    else:
        tmp = 0
    left[i+1] = tmp

tmp = 0
for i in range(n-1, -1, -1):
    if s[i] == '>':
        tmp += 1
    else:
        tmp = 0
    right[i] = tmp

ans = 0
for i in range(n+1):
    ans += max(right[i], left[i])

print(ans)