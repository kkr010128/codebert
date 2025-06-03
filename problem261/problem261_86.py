S=input()
if len(S)%2==0:
    S_mae=S[:len(S)//2]
    S_ushiro=S[len(S)//2:]
else:
    S_mae=S[:len(S)//2+1]
    S_ushiro=S[len(S)//2:]
ans=0
for i in range(len(S_mae)):
    if S_mae[-i-1]!=S_ushiro[i]:
        ans += 1
print(ans)



