input_line = input()
# W,H,x,y,r
input_data = input_line.strip().split(' ')

W, H, x, y, r = [int(i) for i in input_data]

if x < 0 or y < 0:
    print("No")
elif W >= (x+r) and H >= (y+r):
    print("Yes")
else:
    print("No")