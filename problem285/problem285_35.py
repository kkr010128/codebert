s = list(input())
n = len(s) + 1
left = [0]*n
right = [0]*n
for i in range(n-1):
    if s[i] == '<':
        left[i+1] = left[i] + 1
for i in range(n-2, -1, -1):
    if s[i] == '>':
        right[i] = right[i+1] + 1
a = [0]*n
for i in range(n):
    a[i] = max(left[i], right[i])
ans = sum(a)
print(ans)