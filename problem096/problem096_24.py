n,d = map(int,input().split())

p = [list(map(int,input().split())) for i in range(n)]

kyori = d * d
count = 0

for s in range(n):
  nagasa = p[s][0] * p[s][0] + p[s][1] * p[s][1]
  if nagasa <= kyori:
    count += 1
    
print(count)
