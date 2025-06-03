import sys


t = input()
answerCount = 0
stringList = []
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    for i in range(len(str(line).lower().split())):
        stringList.append(str(line).lower().split()[i])

        if str(line).lower().split()[i] == t:
            answerCount += 1



print(answerCount)
