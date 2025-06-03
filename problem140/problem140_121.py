s = list(input())
t = len(s)
if t==1 and s[0]=="?":
    s[0]="D"    
for i in range(t-1):
    if i==0 and s[i]=="?":
        s[i]="D"
        if s[i+1]=="?":
            s[i+1]="D"
    elif s[-1]=="?" and s[-2]=="D" and i==t-2:
        s[-1]="D"
    elif s[i]=="D" and s[i+1]=="?" and s[i+2]=="P":
        s[i+1]="D"
    elif s[i]=="P"  and s[i+1]=="?":
        s[i+1]='D'
    elif s[i]=="D" and s[i+1]=="?":
        s[i+1]='P'

print("".join(s))