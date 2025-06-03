s = input()
n = len(s) // 2
j = -1
t = 0

for i in range(n):
    if s[i] != s[j]:
        t += 1
    j -= 1

print(t)