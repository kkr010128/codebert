K, N = list(map(lambda x: int(x), input().split(" ")))
A = list(map(lambda a: int(a), input().split(" ")))

D = [A[i + 1] - A[i] if i < len(A) - 1 else K - A[i] + A[0] for i in range(len(A))]
D.sort()
print(K - D[-1])