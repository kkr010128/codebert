N,K = map(int,input().split())
H = sorted(map(int,input().split()))
count = N
for i in range(N):
    if H[i]>=K:
        count = i
        break
print(N-count)