inp = list(map(int,input().split()))
w = inp[0]
h = inp[1]
x = inp[2]
y = inp[3]
r = inp[4]
if x+r <= w and x-r >= 0 and y+r <= h and y-r >= 0:
    print("Yes")
else:
    print("No")