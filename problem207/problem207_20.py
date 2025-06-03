A=[list(map(int,input().split())) for _ in range(3)]
N=int(input())
B=[int(input()) for _ in range(N)]
S=[[0,0,0] for _ in range(3)]
for b in B:
  for i in range(3):
    if b in A[i]:
      S[i][A[i].index(b)] = 1
      break
p = False
for a in S:
  if sum(a)==3:
    p = True
    break
if not p:
  for i in range(3):
    if S[0][i]+S[1][i]+S[2][i]==3:
      p = True
      break
if not p:
  if S[0][0]+S[1][1]+S[2][2]==3 or S[2][0]+S[1][1]+S[0][2]==3:
    p=True
print("Yes" if p else "No")