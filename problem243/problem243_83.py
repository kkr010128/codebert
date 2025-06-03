n = int(input())
playList = []
sumTerm = 0
for i in range(n) :
    song = input().split()
    song[1] = int(song[1])
    playList.append(song)
    sumTerm += song[1]
x = input()

tmpSumTerm = 0

for i in range(n) :
    tmpSumTerm += playList[i][1]
    if playList[i][0] == x :
        print(sumTerm - tmpSumTerm)
        break
