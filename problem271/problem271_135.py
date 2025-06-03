N=int(input())
S=list(map(str, input()))
li=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
answer=[]
for i in range(len(S)):
  for j in range(len(li)):
    if S[i]==li[j] and j<len(li)-N:
      answer.append(li[j+N])
    elif S[i]==li[j] and j>=len(li)-N:
      answer.append(li[j+N-len(li)])
print("".join(answer))