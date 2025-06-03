N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

H.sort()
remain = max(0, N-K)
H = H[:remain]

print(sum(H))
