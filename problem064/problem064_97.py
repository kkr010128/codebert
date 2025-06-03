def judge(s,p):

    sList = list(s)
    pList = list(p)


    for i in range(len(sList)):
        if sList[i] == pList[0]:
            answerNum = 0
            counter = i

            for j in range(len(pList)):
                if pList[j] == sList[counter]:
                    answerNum += 1

                    if answerNum == len(pList):
                        return True
                else:
                    break

                if counter == len(sList) -1 :
                    counter = 0
                else:
                    counter += 1
    return False

if judge(input(),input()):
    print("Yes")
else:
    print("No")
