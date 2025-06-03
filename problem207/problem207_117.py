bingoSheet = [0 for x in range(9)]

for i in range(3):
    bingoRow = input().split()
    for j in range(3):
        bingoSheet[i*3 + j] = int(bingoRow[j])

bingoCount = int(input())

responses = []

for i in range(bingoCount):
    responses.append(int(input()))

hasBingo = False

step = 1
initialIndex = 0

for i in range(3):
    firstIndex = i*3
    subList = [bingoSheet[index] for index in [firstIndex, firstIndex+1, firstIndex+2]]
    if (all(elem in responses for elem in subList)):
        hasBingo = True
        break

for i in range(3):
    firstIndex = i
    subList = [bingoSheet[index] for index in [firstIndex, firstIndex+3, firstIndex+6]]
    if (all(elem in responses for elem in subList)):
        hasBingo = True
        break

subList = [bingoSheet[index] for index in [0, 4, 8]]
if (all(elem in responses for elem in subList)):
    hasBingo = True

subList = [bingoSheet[index] for index in [2, 4, 6]]
if (all(elem in responses for elem in subList)):
    hasBingo = True

if hasBingo:
    print('Yes')
    quit()

print('No')
quit()
