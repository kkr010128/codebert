import sys

data = sys.stdin.readline().strip().split(' ')
a = int(data[0])
b = int(data[1])
c = int(data[2])

cnt = 0
for i in range(a, b+1):
    if c % i == 0:
        cnt += 1

print(cnt)