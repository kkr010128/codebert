S = str(input())
T = str(input())
lenS = len(S)
lenT = len(T)
splitS = []

for i in range(lenS - lenT +1):
    tempS = S[i : i+lenT]
    splitS.append(tempS)

answer = lenT
for tempS in splitS:
    count = 0
    for i in range(lenT):
        if tempS[i] != T[i]:
            count += 1
    answer = min(answer, count)
print(answer)