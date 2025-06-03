inData = int(input())
inSeries = [int(i) for i in input().split()]
outData =[0]*inData

for i in range(inData):
    outData[i] = inSeries[inData-1-i]

print(" ".join(map(str,outData)))
