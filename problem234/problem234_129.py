import sys
input = sys.stdin.readline

a = input()

n = int(a)

s = [[0] * 9 for _ in range(9)]

for i in range(1, n+1):
    j = str(i)
    k = int(j[0])
    l = int(j[-1])
    if l != 0:
        s[k-1][l-1] += 1

ans = 0

#print(s)

for i in range(1, 10):
    for j in range(1, 10):
        ans += s[i-1][j-1] * s[j-1][i-1]

print(ans)
