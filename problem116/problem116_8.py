S=input()
T=input()
cnt=0
for idx in range(len(S)):
  if S[idx]==T[idx]:
    cnt=cnt
  else:
    cnt=cnt+1
print(cnt)