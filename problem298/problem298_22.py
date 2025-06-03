MM = input().split()
N = int(MM[0])
K = int(MM[1])
HH = input().split()
total = 0
for i in HH:
  if int(i) >= K:
    total +=1
print(total)