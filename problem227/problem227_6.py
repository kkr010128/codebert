N,K=map(int,input().split())
List = list(map(int, input().split()))
List.sort(reverse = True)
res = 0
for i in range(N):
  if i <= K-1:
    pass
  else:
    res += List[i]
print(res)