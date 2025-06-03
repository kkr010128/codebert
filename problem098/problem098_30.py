from sys import stdin
N = int(stdin.readline().rstrip())
C = stdin.readline().rstrip()
rc = C.count('R')
ans = 0
for i in range(rc):
    if C[i] == 'W':
        ans += 1
print(ans)