t=list(input())

if t[0]=="?":
    if len(t)<=2:
        t[0]="D"

    elif t[1]=="P":
        t[0]="D"
    
    else:
        t[0]="P"
for i in range(1,len(t)):
    if t[i]=="?":
        if i+1==len(t):
            t[i]="D"
            break
        if t[i-1]=="P":
            t[i]="D"
        else:
            if t[i+1]=="P":
                t[i]="D"
            else:
                t[i]="P"
b=""
for i in range(len(t)):
    b+=t[i]
print(b)
    
