S=input()
t=len(S)
print("YNeos"[sum(1for i in range(t) if S[i]!=S[~i] )!=0 or S[(t+2)//2:]!=S[:(t-1)//2]::2])