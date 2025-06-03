N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
count = 0
for i in range(0, N-K):
    count += H[i]

print(count)
