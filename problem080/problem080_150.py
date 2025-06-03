n, *XY = map(int, open(0).read().split())
XY = list(zip(XY[::2], XY[1::2]))
A = [x+y for x, y in XY]
B = [x-y for x, y in XY]
print(max(max(A) - min(A), max(B) - min(B)))