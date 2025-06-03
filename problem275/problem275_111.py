x,y=map(int,input().split())
print(100000*(max(4-x,0)+max(4-y,0)+4*(x==y==1)))