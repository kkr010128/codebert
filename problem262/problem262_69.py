N = int(input())
XYList = []
for i in range(N):
    A = int(input())
    XY = []
    for j in range(A):
        XY.append(list(map(int, input().split())))
    XYList.append(XY)
maxSum = 0
for i in range(2**N):
    sum = 0
    for j in range(N):
        if i >> j & 1:
            honest = True
            for XY in XYList[j]:
                if ((i >> (XY[0]-1)) & 1) != XY[1]:
                    honest = False
                    break
            if honest:
                sum += 1
            else:
                sum = 0
                break
    if maxSum < sum:
        maxSum = sum
print(maxSum)