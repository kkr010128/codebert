k,n = map(int,input().split())

Ai = list(map(int,input().split()))
kyori = []

for x in range(n-1):
  kyori.append(Ai[x+1]-Ai[x])
  
kyori.append(Ai[0]+k-Ai[n-1])

kyori.remove(max(kyori))

print(sum(kyori))
