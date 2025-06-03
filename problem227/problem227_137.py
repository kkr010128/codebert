_, K = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]

H.sort(reverse=True)
print(sum(H[K:]))