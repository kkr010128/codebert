import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
n, k = map(int, readline().split())
r, s, p = map(int, readline().split())
t = readline().decode().rstrip()

t = list(t)

for i in range(k, n):
    if t[i] == t[i - k]:
        t[i] = 0

ans = t.count('r') * p + t.count('p') * s + t.count('s') * r
print(ans)