n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
C = [abs(X[i] - Y[i]) for i in range(n)]
D = []
def distance(X, Y):  
  for k in range(1, 4):
    d = 0
    for j in range(len(X)):
      d += C[j] ** k
    d = d ** (1 / k)
    D.append(d)
  D.append(max(C))
  return D

distance(X, Y)
for i in range(4):
  print('{:.08f}'.format(D[i]))
