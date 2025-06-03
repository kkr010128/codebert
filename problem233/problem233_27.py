n=int(input())
a=list(map(int, input().split()))
mi = n+2
ans = 0
for i in a:
   if mi > i:
      ans+=1
      
   mi=min(i,mi)

print(ans)