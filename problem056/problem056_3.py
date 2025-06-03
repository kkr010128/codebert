#データ入力
rowNum, columnNum = map(int, input().split())
inMat = [[0] * columnNum for i in range(rowNum)]
inColumnVec = [[0] for i in range(columnNum)]
for row in range(rowNum):
    inMat[row] = [int(i) for i in input().split()]
for column in range(columnNum):
    inColumnVec[column] = int(input())

timesAns = [[0] for i in range(rowNum)]

#行列計算
for row in range(rowNum):
    timesAns[row] = 0
    for column in range(columnNum):
        timesAns[row] = timesAns[row] + inMat[row][column] * inColumnVec[column]

for row in range(rowNum):
    print(timesAns[row])
