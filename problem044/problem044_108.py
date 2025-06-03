import sys
a, b, c = map(int, sys.stdin.readline().strip().split())
cnt = 0
for i in range(a, b+1):
    if c % i == 0:
        cnt += 1
    else:
        continue

print(cnt)