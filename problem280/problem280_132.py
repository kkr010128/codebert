N = int(input())
ct = []
 
for i in range(N):
  ct.append([int(i) for i in input().split()])
 
dist = 0
for a in ct:
  for b in ct:
    dist += (abs(a[0] - b[0])**2 +abs(a[1] - b[1])**2)**0.5
print(dist/N)
