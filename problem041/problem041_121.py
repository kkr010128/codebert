W,H,x,y,r=[int(x) for x in input().split()]
print("No" if x < r or y < r or (x+r) > W or (y+r) > H else "Yes")
