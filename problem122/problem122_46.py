import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]
count = [0] * 10**5
for i in range(N):
        count[A[i]-1] += 1

Q = int(input())
ans = sum(A)
for i in range(Q):
    B, C = map(int, input().split())
    ans += (C - B) * count[B-1]

    print(ans)

    count[C-1] += count[B-1]
    count[B-1] = 0