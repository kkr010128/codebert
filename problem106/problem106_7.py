N = int(input())
A = [0] * (N + 1)
for i in range(1, 102):
    for j in range(1, 102):
        for k in range(1, 102):
            t = i ** 2 + j ** 2 + k ** 2 + i * j + j * k + i * k
            if t <= N:
                A[t] += 1
for n in range(1, N + 1):
    print(A[n])