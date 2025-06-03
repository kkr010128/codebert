N, A, B = input().split(' ')
N = int(N)
A = int(A)
B = int(B)
a = A * (N // (A+B))
if (N%(A+B)) > A:
  a += A
else:
  a += (N%(A+B))
print(a)