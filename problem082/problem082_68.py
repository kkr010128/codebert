S=input()
T=input()
s=len(S)
t=len(T)
A=[]


for i in range(s-t+1):
  word=S[i:i+t]
  a=0
  for j in range(t):
    if word[j]==T[j]:
      a+=1
    else:
      a+=0
  A.append(t-a)

print(min(A))