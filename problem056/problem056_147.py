n, m = list(map(int, input().split()))

A = [list(map(int, input().split())) for i in range(n)]
bt = [int(input()) for i in range(m)]

for i in range(n):
    print(sum([x * y for (x, y) in zip(A[i], bt)]))
   
