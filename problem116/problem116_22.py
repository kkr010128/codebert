S=input()
T=input()
total=0
for i in range(0,len(S)):
    if S[i]!=T[i]:
        total+=1
print(int(total))