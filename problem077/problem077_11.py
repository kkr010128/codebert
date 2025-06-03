l=list(map(int, input().split()))
l1=[l[0],l[1]]
l2=[l[2],l[3]]
ans=l[0]*l[2]
for i in l1:
  for j in l2:
    if i*j>ans:
      ans=i*j
print(ans)
