n = int(input())
L = list(map(int,input().split(' ')))
L.sort()

ans = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if L[i]==L[j]:
        continue
      if L[j]==L[k]:
        continue
      if L[i]+L[j] <= L[k]:
        continue
      ans+=1

print(ans)
