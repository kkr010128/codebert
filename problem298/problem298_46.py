N,K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)

cnt = 0
for h in H:
  if h >= K:
    cnt += 1
  else:
    break
print(cnt)
