N, A, B = map(int, input().split())
r = (N//(A+B))*A
N = N%(A+B)
print(r+N if N<=A else r+A)
