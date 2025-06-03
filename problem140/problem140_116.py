T=input()
list=[]
for j in range(len(T)):
    if T[j]=="?":
        list.append(j)
tt=[]
for TT in range(len(T)):
    tt.append(T[TT])
for i in list:
    tt[i]="D"
answer=""
for p in range(len(T)):
    answer+=tt[p]
print(answer)