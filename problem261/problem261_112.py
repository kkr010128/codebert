S=list(str(input()))
a=0
if len(S)%2==0:
    for i in range((len(S))//2):
        if S[i]!=S[len(S)-i-1]:
            a+=1
if len(S)%2==1:
    for i in range((len(S)-1)//2):
        if S[i]!=S[len(S)-i-1]:
            a+=1
print(a)