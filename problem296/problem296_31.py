S=list(input())
K=int(input())
cnt=cnt2=0
s=S*2
if len(set(S))==1:
    print(len(S)*K//2);exit()
for i in range(len(S)-1):
    if S[i+1]==S[i]:
        cnt+=1
        S[i+1]="#"
for i in range(len(s)-1):
    if s[i+1]==s[i]:
        cnt2+=1
        s[i+1]="#"
print(cnt+(cnt2-cnt)*(K-1))