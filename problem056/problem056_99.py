n,m = map(int, raw_input().split())
A = []
B = []

for i in range(n):
        A.append(map(int, raw_input().split()))
for i in range(m):
        B.append(input())

for i in range(n):
        answer = 0
        for j in range(m):
                answer += A[i][j] * B[j]
        print answer