from sys import stdin
A, B, C = [int(_) for _ in stdin.readline().rstrip().split()]
K = int(stdin.readline().rstrip())
for i in range(K):
    if not B > A:
        B *= 2
    elif not C > B:
        C *= 2
if A < B < C:
    print("Yes")
else:
    print("No")