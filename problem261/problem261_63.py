# 147 B

s = input()
k = s[::-1]
n = 0

for i in range(len(s)):
    if s[i] != k[i]:
        n += 1
        # print(s[i])

print(n // 2) 
