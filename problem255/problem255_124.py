N = int(input())
S,T = input().split()
L = []

for n in range(N):
  L.append(S[n])
  L.append(T[n])
  
print(*L,sep="")