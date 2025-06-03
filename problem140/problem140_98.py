import sys
input = sys.stdin.readline

t = list(input())
t.pop()
n = len(t)

res = 0
for i in range(n):
    if t[i] == '?':
        t[i] = 'D'

print(''.join(t))

