N = int(input())
A = [[[0] * 10, [0] * 10, [0] * 10], [[0] * 10, [0] * 10, [0] * 10], [[0] * 10, [0] * 10, [0] * 10], [[0] * 10, [0] * 10, [0] * 10]]

for i in range(N):
    b, f, r, v = [int(j) for j in input().split()]
    A[b-1][f-1][r-1] += v

for a, b in enumerate(A):
    for f in b:
        print(' ' + ' '.join([str(i) for i in f]))
    else:
        if a != len(A) - 1:
            print('#' * 20)