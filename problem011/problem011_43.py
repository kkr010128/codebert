twoNumbers=list(map(int,input().split()))
x=twoNumbers[0]
y=twoNumbers[1]
devidedBy=[]
syou=[]
if x>=y:
    for number in range(1, y+1):
        if y%number==0:
            if number>y//number:
                break
            else:
                if not number in devidedBy:
                    devidedBy.append(number)
                if not y//number in syou:
                    syou.append(y//number)
else:
    for number in range(1, x+1):
        if x%number==0:
            if number>x//number:
                break
            else:
                if not number in devidedBy:
                    devidedBy.append(number)
                if not x//number in syou:
                    syou.append(x//number)

if devidedBy[len(devidedBy)-1]==syou[len(syou)-1]:
    del devidedBy[len(devidedBy)-1]

devidedBy.extend(syou)
devidedBy.sort()
index=len(devidedBy)-1
while index>=0:
    if x>=y:
        if x%devidedBy[index]==0:
            print(devidedBy[index])
            break
        else:
            index-=1
    else:
        if y%devidedBy[index]==0:
            print(devidedBy[index])
            break
        else:
            index-=1
