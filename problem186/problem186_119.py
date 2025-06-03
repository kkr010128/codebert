K, N = map(int,input().split())
A = [int(a) for a in input().split()]

dif = [A[i+1] - A[i] for i in range(N-1)]

dif.append(K + A[0] - A[N-1])

print(K - max(dif))