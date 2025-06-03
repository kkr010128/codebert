n = int(input())
s = list(map(int, input().strip().split(' ')))
t = n // 2

for i in range(0, n // 2):
    s[i], s[n - i - 1] = s[n - i - 1], s[i]

for i in range(0, len(s)):
    if i != len(s) - 1:
        print(s[i], end=" ")
    else:
        print(s[i])
