N=int(input())
L=list(map(int,input().split()))
s=0
R=list()
for i in range(N):
  s=s^L[i]
for i in range(N):
  R.append(str(s^L[i]))
print(" ".join(R))