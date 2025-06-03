s = input()

right = [0]*(len(s)+1)
for i in range(len(s)):
    if s[i] == '<':
        right[i+1] = right[i] + 1

left = [0]*(len(s)+1)
for i in range(len(s)-1, -1, -1):
    if s[i] == '>':
        left[i] = left[i+1] + 1

ans = 0
for i in range(len(s)+1):
    ans += max(right[i], left[i])

print(ans)