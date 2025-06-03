N,K = map(int,input().split())
H = list(map(int,input().split()))
H = sorted(H)[::-1]
H = H[K:N]
print(str(sum(H)))