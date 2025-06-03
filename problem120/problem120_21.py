n,k=map(int,input().split())
p=list(map(int,input().split()))
p_list=sorted(p, reverse=False)
sum=0
for i in range(k):
  sum+=p_list[i]
print(sum)