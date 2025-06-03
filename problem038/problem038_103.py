inputStr = input()
numList = inputStr.split(' ')
numList = [int(x) for x in numList]

#print('a: ',numList[0])
#print('b: ',numList[1])

if numList[0]==numList[1]:
    print('a == b')
elif numList[0]>numList[1]:
    print('a > b')
elif numList[0]<numList[1]:
    print('a < b')