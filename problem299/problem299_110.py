N = int(input())
A = list(map(int, input().split()))

l = {a: i for i, a in enumerate(A, start=1)}
print(' '.join([str(l[i+1]) for i in range(N)]))
