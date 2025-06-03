n,m=map(int,input().split())
height=list(map(int,input().split()))
hoge=[1 for i in range(n)]
#print(hoge)
for i in  range(m):
  a,b=map(int,input().split())
  #print(a,b,height[a-1],height[b-1])
  if(height[a-1]>height[b-1]):
    hoge[b-1]=0
  elif(height[a-1]<height[b-1]):
    hoge[a-1]=0
  else:
    hoge[a-1],hoge[b-1]=0,0
    
print(sum(hoge))