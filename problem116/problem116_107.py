S=input()
T=input()
S=list(S)
T=list(T)
sum=0
for i in range(len(S)):
  if not S[i]==T[i]:
    sum += 1
print(sum)