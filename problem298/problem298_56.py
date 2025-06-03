N,K = map(int,input().split())
h = list(map(int,input().split()))
cnt = 0
hei = 0
for i in range(N):
  hei = h[i]
  if hei >= K:
    cnt += 1
print(cnt)