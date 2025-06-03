WHxyr = input().split()
W = int(WHxyr[0])
H = int(WHxyr[1])
x = int(WHxyr[2])
y = int(WHxyr[3])
r = int(WHxyr[4])


if x-r<0 or x+r>W or y-r<0 or y+r>H:
    print("No")
else:
    print("Yes")