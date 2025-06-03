import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
l = [A[0]]

for i in range(1, N):
    l.append(A[i])
    l.append(A[i])

print(sum(l[:N-1]))