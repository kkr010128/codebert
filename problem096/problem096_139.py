S = 0
N,D = input().split()
N = int(N)
D = int(D)
X = [0]*N
Y = [0]*N
for i in range(N):
  X[i],Y[i] = map(int, input().split())
  if ((X[i])**2 + (Y[i])**2) <= (D)**2:
    S = S + 1
print(S)