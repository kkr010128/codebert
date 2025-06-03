N, X, Y = map(int, input().split())
ans = [0]*N

for i in range(1,N+1):
  for j in range(i+1,N+1):
    d = min(j-i,abs(i-X)+abs(j-Y)+1)
    #print(i,j,d)
    ans[d]+=1

print(*ans[1:], sep='\n')
