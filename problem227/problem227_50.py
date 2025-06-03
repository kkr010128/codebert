N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
H = sorted(H, reverse=True)
for i in range(min(K,len(H))):
  H[i] = 0
print(sum(H))