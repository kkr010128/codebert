N,M = [int(x) for x in input().split()]
S = list(input())
S1 = S[::-1]
ind = 0
ans = []
while ind!=N:
  ind1 = ind
  for i in range(M,0,-1):
    if ind+i<=N and S1[ind+i]=="0":
      ind = ind+i
      ans.append(i)
      break
  if ind1==ind:
    print(-1)
    exit()
print(*ans[::-1])