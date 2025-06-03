a,b,c,d = map(int, input().split())

ans = -10**18+1
for i in [a,b]:
  for j in [c,d]:
    if ans < i*j: ans = i*j
print(ans)