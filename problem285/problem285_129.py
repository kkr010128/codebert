s=input()
n=len(s)
ans=0
currentstreak=0
numberbefore=0
legacy=0
for i in range(n):
  if s[i]=='<':
    numberbefore+=1
    ans+=numberbefore
    currentstreak=0
    legacy=numberbefore
  else:
    currentstreak+=1
    ans+=currentstreak
    if currentstreak<=legacy:
      ans-=1
    numberbefore=0
print(ans)