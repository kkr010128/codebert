S=str(input())
n=len(S)
Srev=''.join(list(reversed(S)))
S1=S[0:(n-1)//2]
S2=S[((n+1)//2):n]
S1rev=''.join(list(reversed(S1)))
S2rev=''.join(list(reversed(S2)))
if S==Srev and S1==S1rev and S2==S2rev:
    print('Yes')
else:
    print('No')