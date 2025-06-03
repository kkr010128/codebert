N=int(input())
rep=0
result="No"
for i in range(N):
  a,b=map(int,input().split())
  if a==b:
    rep+=1
  else:
    rep=0
  if rep==3:
    result="Yes"
    break
print(result)    