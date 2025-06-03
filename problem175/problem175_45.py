n = int(input())
s = input()
ans = s.count('R') * s.count('G') * s.count('B')

for i in range(n):
    for j in range(i + 1, n):
        if j * 2 - i >= n:
            continue
        if s[i] == s[j] or s[j] == s[2 * j - i] or s[i] == s[2 * j - i]:
            continue
        ans -= 1

print(ans)
