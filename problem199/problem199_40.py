S=input()
ans='Yes'
i=0
while i<len(S):
    if S[i:i+2]!='hi':
        ans='No'
    i+=2
print(ans)