N = int(input())
C = input()

WL = [0]
RR = [C.count('R')]

for i in range(0, N):
    if C[i] == 'R':
        WL.append(WL[i])
        RR.append(RR[i] - 1)
    else:
        WL.append(WL[i] + 1)
        RR.append(RR[i])

MM = N
for i in range(0, N + 1):
    MM = min(MM, (max(WL[i], RR[i])))
print(MM)