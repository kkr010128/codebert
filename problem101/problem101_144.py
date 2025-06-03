clr = list(map(int, input().split()))
k = int(input())

for i in range(k):
    if clr[2] <= clr[1] :
        clr[2] *= 2
    
    elif clr[1] <= clr[0]:
        clr[1] *= 2
    
    else:
        break
    
if clr[2] > clr[1] > clr[0] :
    print("Yes")
else:
    print("No")