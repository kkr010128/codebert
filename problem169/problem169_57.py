N = int(input())
A = tuple(map(int, input().split()))
x = [0] * N
for i in range(N - 1):
    x[A[i]-1] += 1
for a in x:
    print(a)