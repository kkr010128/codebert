S=list(input())
N=len(S)
x=0
for i in range(int((N-1)/2)):
    if S[i]!=S[-(i+1)]:
        print("No")
        break
    elif i==int((N-1)/2)-1:
        x+=1
import math
if x==1:
    S_l=S[:int((N-1)/2)]
    for i in range(int(math.ceil(len(S_l)/2))):
        if S_l[i]!=S_l[-(i+1)]:
            print("No")
            break
        elif i==int(math.ceil(len(S_l)/2))-1:
            x+=1
if x==2:
    S_m=S[int((N+3)/2)-1:N]
    for i in range(int(math.ceil(len(S_m)/2))):
        if S_m[i]!=S_m[-(i+1)]:
            print("No")
            break
        elif i==int(math.ceil(len(S_m)/2))-1:
            print("Yes")