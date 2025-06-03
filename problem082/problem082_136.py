s=input()
t=input()
scorelist=[]
for i in range(len(s)-len(t)+1):
  S=s[i:i+len(t)]
  score=0
  for j in range(len(t)):
    if S[j]!=t[j]:
      score+=1
  scorelist.append(str(score))
point=min(scorelist)
print(point)
