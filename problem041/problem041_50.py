W,H,x,y,r=map(int,raw_input().split())
print'Yes' if((0+r)<=x and (W-r)>=x) and ((0+r)<=y and (H-r)>=y) else'No'