midScore =[0]*50
finScore = [0]*50
reScore = [0]*50
personNum = 0
while True:
    m,f,r = map(int,input().split())
    midScore[personNum] = m
    finScore[personNum] = f
    reScore[personNum] = r
    personNum += 1
    if m is f is r is -1:
        break
    
    
for person in range(personNum):
    totalScore = midScore[person] + finScore[person]
    if midScore[person] is finScore[person] is reScore[person] is -1:
        pass
    elif midScore[person] == -1 or finScore[person] == -1:
        print("F")
    elif 80<=totalScore:
        print("A")
    elif 65<=totalScore<80:
        print("B")
    elif 50<=totalScore<65:
        print("C")
    elif 30<=totalScore<50:
        if 50<=reScore[person]:
            print("C")
        else:
            print("D")
    elif totalScore<30:
        print("F")
