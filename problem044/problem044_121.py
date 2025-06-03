from sys import stdin

a, b, c = (int(n) for n in stdin.readline().rstrip().split())

cnt = 0

for n in range(a, b + 1):
    if c % n == 0:
        cnt += 1

print(cnt)

