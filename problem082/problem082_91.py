S = list(input())
T = list(input())

mindiff = len(S)
for i in range(len(S) - len(T) +1):
    diff = 0
    for j in range(len(T)):
        if(S[i+j] != T[j]):
            diff += 1
        pass
    if(diff < mindiff):
        mindiff = diff

print(mindiff)



