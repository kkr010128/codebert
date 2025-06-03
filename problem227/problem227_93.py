n, k = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
print(sum(H[:max(n-k, 0)]))