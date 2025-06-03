T=input()
ans=""
if T=="?":
    print("D")
    exit()

for i in range(len(T)):
    if T[i]=="P" or T[i]=="D":
        ans+=T[i]
    else:
        if i==0:
            if T[i+1]=="P":
                ans+="D"
            elif T[i+1]=="D":
                ans+="P"
            elif T[i+1]=="?":
                ans+="P"
        elif i!=len(T)-1:
            if ans[-1]=="P" and T[i+1]=="P":
                ans+="D"
            elif ans[-1]=="P" and T[i+1]=="D":
                ans+="D"
            elif ans[-1]=="P" and T[i+1]=="?":
                ans+="D"
            elif ans[-1]=="D" and T[i+1]=="P":
                ans+="D"
            elif ans[-1]=="D" and T[i+1]=="D":
                ans+="P"
            elif ans[-1]=="D" and T[i+1]=="?":
                ans+="P"
        else:
            if ans[-1]=="P":
                ans+="D"
            else:
                ans+="D"
print(ans)