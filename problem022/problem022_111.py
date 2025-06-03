import sys

n = sys.stdin.readline()
s = sys.stdin.readline().split()
q = sys.stdin.readline()
t = sys.stdin.readline().split()
cnt = 0

for i in t:
    if i in s:
        cnt += 1

print(cnt)