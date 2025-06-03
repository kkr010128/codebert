from sys import stdin

n = int(input())
S = stdin.readline().split()
q = int(input())
T = stdin.readline().split()

cnt = 0
for x in T:
    if x in S:
        cnt += 1

print(cnt)
