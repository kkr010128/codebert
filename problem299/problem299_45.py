from sys import stdin

n = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

ans = [0] * n

for i, a in enumerate(A):
    ans[a-1] = i+1

print(' '.join(map(str, ans)))