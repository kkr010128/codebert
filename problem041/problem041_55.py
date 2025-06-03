W,H,x,y,r=map(int,input().split())
print('Yes') if x+r<=W and y+r<=H and r<=x and r<=y else print('No')
