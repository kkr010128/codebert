N=int(input())
A_list=sorted(list(map(int, input().split())), reverse=True)
ans=1

for a in A_list:
  ans*=a
  if ans>1e+18:
    ans=-1
    break
if 0 in A_list:
  ans=0
print(ans)



