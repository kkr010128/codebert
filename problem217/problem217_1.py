n = int(input())
numlist = map(int, input().split())
numarr = list(numlist)
isevenList = [i for i in numarr if i % 2 == 0]
answerList = []
for i in isevenList:
    if i % 3 == 0 or i % 5 == 0:
        answerList.append("APPROVED")
    else:
        answerList.append("DENIED")
if "DENIED" in answerList:
    print("DENIED")
else:
    print("APPROVED")