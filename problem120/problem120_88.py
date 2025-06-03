X,Y = map(int,input().split())
MMM = map (int,input().split())
MM = list(MMM)
MM.sort()
total = 0
for i in range(Y):
  total += MM[i]
print(total)
