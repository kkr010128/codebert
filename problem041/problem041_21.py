W, H, x, y, r = map(int, raw_input().split())
if x-r<0 or y-r<0:
    print"No"

elif x+r <= W and y+r <= H:
    print"Yes"
else:
    print"No"