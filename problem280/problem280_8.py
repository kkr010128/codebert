import itertools

N = int(input())
c = []
d = 0


for i in range(N):
  x1, y1 = map(int, input().split())
  c.append((x1,y1))
  
cp = list(itertools.permutations(c))
x = len(cp)

for i in range(x):
  for j in range(N-1):
  	d += ((cp[i][j][0]-cp[i][j+1][0])**2 + (cp[i][j][1] - cp[i][j+1][1])**2)**0.5
  
  
print(d/x)