#ABC172-B
S = str(input())
T = str(input())
L = int(len(T))
for i in range(L):
  if S[i] == T[i]:
    L -= 1
print(L)