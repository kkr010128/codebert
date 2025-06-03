T=str(input())
T2=list(T)
if T2[0]=="?":
    T2[0]="D"

if T2[len(T)-1]=="?":
    T2[len(T)-1]="D"

for i in range(1,len(T2)-1):
    if T2[i]=="?":
        if T2[i-1]=="D" and T2[i+1]!="P":
            T2[i]="P"
            
        else:
            T2[i]="D"
ans="".join(T2)    
print(ans)