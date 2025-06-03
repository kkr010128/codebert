import array

N = int(input())
A = array.array('L', list(map(int, input().split())))
MAX = 10**5+1
X = array.array('L', [0]) * MAX
Y = array.array('L', range(MAX))

for i in range(len(A)): X[A[i]] += 1
    
Q = int(input())
cur = sum(array.array('L', (X[i]*Y[i] for i in range(len(X)))))

for i in range(Q):
    [b, c] = list(map(int, input().split()))
    cur = cur - X[b]*b + X[b]*c
    print(cur)
    X[c] += X[b]
    X[b] = 0

