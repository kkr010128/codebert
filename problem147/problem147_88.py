#A
S=input()
T=input()
ans='No'
if S != T:
    if S==T[:(len(S))]:
        if T[-1].islower():
            ans='Yes'
print(ans)
