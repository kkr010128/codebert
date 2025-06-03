N, D = map(int, input().split())
X = [list(map(int, input().split())) for l in range(N)]
count = 0

for i in range(N):
  if (X[i][0])**2 + (X[i][1])**2 - D**2 <= 0:
    count = count + 1
    
print(count)
