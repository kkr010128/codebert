n = int(input())
numList = map(int,input().split())
numList = list(numList)

multiplyList = []
start = 0
for i in range(n+1):
    start += 1
    for j in range(start, n):
        multiplyList.append(numList[i] * numList[j])

print(sum(multiplyList))