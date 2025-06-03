input_data = input().split(' ')

W, H, x, y, r = [int(i) for i in input_data]

if ((x-r) >= 0 and (y-r) >= 0) and (W >= (x+r) and H >= (y+r)):
    print("Yes")
else:
    print("No")