N=input()
L=[int(N[i]) for i in range(len(N))]

P=0
OT=0

for i in range(len(L)-1):
    if 0 <= L[i] <= 3:
        P += L[i] + OT
        OT = 0

    elif L[i] == 4:
        if OT == 1 and L[i+1]>=5:
            P += 5
        else:
            P += OT+L[i]
            OT = 0

    elif L[i] == 5:
        if OT == 1:
            P += 4

        else:
            if L[i+1] >= 5:
                P += 1 + 4
                OT = 1
            else:
                P += 5

    else:
        if OT == 1:
            P += 9-L[i]
            OT = 1
        else:
            P += 10 - L[i]
            OT = 1

Pone = 0
if OT==0:
    Pone = min(L[-1],11-L[-1])
elif OT==1 and L[-1]<=4:
    Pone = 1+L[-1]
else:
    Pone = 10-L[-1]

print(P+Pone)