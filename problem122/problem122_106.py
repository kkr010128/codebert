sum = 0
num = [0] * (10 ** 5 + 1)
N = int(input())
A = [int(a) for a in input().split()]
for i in range(0, N):
    sum += A[i]
    num[A[i]] += 1

Q = int(input())
for i in range(0, Q):
    B, C = (int(x) for x in input().split())
    sum += (C - B) * num[B]
    num[C] += num[B]
    num[B] = 0
    print(sum)