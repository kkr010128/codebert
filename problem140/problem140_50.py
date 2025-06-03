S=input()
ans=[]
for i in range(len(S)):
    if S[i]=="?":
        ans.append("D")
    else:
        ans.append(S[i])
print("".join(ans))