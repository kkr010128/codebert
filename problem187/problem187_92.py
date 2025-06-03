n,x,y=map(int,input().split())

#最短距離が１の時２の時、、、という風に実験しても途方に暮れるだけだった
#i,j固定して最短距離がどう表せるかを考える
def min_route_count(i,j):
  return min(abs(j-i),abs(j-y)+1+abs(x-i))

ans_list=[0]*(n-1)
for i in range(1,n):
  for j in range(i+1,n+1):
    ans_list[min_route_count(i,j)-1]+=1
    
for t in range(n-1):
  print(ans_list[t])
