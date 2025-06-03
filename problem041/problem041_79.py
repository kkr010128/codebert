W,H,x,y,r=map(int,input().split())
print('Yes'if(False if x<r or W-x<r else False if y<r or H-y<r else True)else'No')
