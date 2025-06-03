N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

H.sort(reverse=True)

s = 0
for i in range(K, N):
    s += H[i]

print(s)