l,r,d=map(int,input().split())
print(len([i for i in range(l,r+1) if i%d==0]))