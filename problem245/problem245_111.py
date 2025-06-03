n=int(input())
s=input()
c=0
for i in range(n-2):
    if s[i]=="A":
        if s[i+1]=="B":
            if s[i+2]=="C":
                c+=1
            else:
                pass
        else:
            pass
    else:
        pass
print(c)