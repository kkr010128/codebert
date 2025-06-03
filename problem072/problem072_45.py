N = int(input())
D = []
count = 0

for i in range(N):
  d = list(map(int,input().split()))
  D.append(d)
  
for i in range(N-2):
  if (D[i][0]==D[i][1]) and (D[i+1][0]==D[i+1][1]) and (D[i+2][0]==D[i+2][1]):
    print("Yes")
    break
else:
  print("No")
