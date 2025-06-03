N, K = map(int, input().split())
H = list(map(int, input().split()))
A = [i for i in H if i >= K]
print(len(A))