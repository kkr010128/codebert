n,k = map(int,input().split())
count = 0

p = map(int,input().split()) 
P = sorted(p)

for k in range(k):
  count = count + int(P[k])

print(count)
