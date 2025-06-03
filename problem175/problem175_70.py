n = int(input())
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')

cnt = 0
for i in range(n):
    j = 1
    while i + 2*j <= n-1:
        if s[i] != s[i+j] and s[i+j] != s[i+2*j] and s[i+2*j] != s[i]:
            cnt += 1
        j += 1

print(r*g*b-cnt)