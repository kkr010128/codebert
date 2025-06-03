a=[s for s in input()]*2
b=input()
w=False
for j in range(len(a)):
    if a[j]==b[0]:
        total=1
        if len(b)==1:
            print("Yes")
            w=True
            break
        for i in range(1,len(b)):
            if j+i==len(a):
                print("No")
                w=True
                break
            else:
                if a[j+i]==b[i]:
                    total+=1
                    if total==len(b):
                        print("Yes")
                        w=True
                        break
                else:
                    break
    if w==True:
        break
if w==False:
    print("No")
