import sys
input = sys.stdin.readline

n, s, c = int(input()), list(map(int, input().split())), 0
m = s[0]
for i in range(n):
	if s[i] <= m: m = s[i]; c += 1
print(c)