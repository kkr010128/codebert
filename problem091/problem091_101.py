n = int(input())
l = list(map(int, input().split()))
ans=0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      li = [l[i], l[j], l[k]]
      
      m = max(li)
      if 2*m < sum(li) and len(set(li)) == 3:
        ans += 1
print(ans)