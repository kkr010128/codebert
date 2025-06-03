import math

s = input()
n = len(s)
cnt = 0

for i in range(n):
    if(s[i] != s[n-1-i]):
        cnt = cnt + 1

print(math.ceil(cnt/2))


