S=input()
i=0
kot=[]
for a in S:
    kot.append(a)
tok=list(reversed(kot))

for a in range(len(kot)):
    if kot[a]==tok[a]:
        i=0
    else:
        print("No")
        i=1
        break
if i==0:
    for a in range(int((len(kot)-1)/2)):
        if kot[a]==tok[int((len(kot)-1)/2)-a-1]:
            i=0
        else:
            print("No")
            i=1
            break

if i==0:
        for a in range(int((len(kot)-1)/2)):
            if kot[int((len(kot)+3)/2)+a-1]==tok[-a-1]:
                i=0

            else:
                print("No")
                i=1
                break

if i==0:
    print("Yes")
