N, K = map(int, input().split())
cad = N // K
n = N - K * cad
m = K * (cad + 1) - N
print(min(n, m))