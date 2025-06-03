S=input()
N=len(S)
S=list(S)
ct=0
for i in range(N//2):
  if S[i]!=S[-i-1]:
    ct+=1
print(ct)