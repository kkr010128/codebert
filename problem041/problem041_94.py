ins = input().split()
w = int(ins[0])
h = int(ins[1])
x = int(ins[2])
y = int(ins[3])
r = int(ins[4])
if x - r >= 0 and y - r >= 0 and x + r <= w and y + r <= h:
    print("Yes")
else:
    print("No")