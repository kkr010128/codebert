N, K = map(int, input().split())

n = N%K
m = K - n

print(min(abs(n), abs(m)))