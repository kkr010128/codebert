K=int(input())
l=list(input())
c=0
for i in range(K-2):
    if l[i]=="A":
        if l[i+1]=="B":
            if l[i+2]=="C":
                c+=1
print(c)