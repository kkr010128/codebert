n=int(input())
a=list(map(int,input().split()))
j=1
for i in a:
  if j==i:j+=1
print([n-j+1,-1][j==1])