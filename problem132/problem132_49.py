import math
N, K = map(int, input().split())
lightPow = list(map(int, input().split()))

for i in range(K):
  newLightPow = [0]*(N+1)
  #print(lightPow)
  for pos in range(1, N+1):
    low = pos - lightPow[pos-1]
    high = pos + lightPow[pos-1]
    low = min(max(1, low), N)
    high = min(max(1, high), N)
    newLightPow[low-1] += 1
    newLightPow[high] -= 1
    #print("pos:"+str(pos))
    #print("low"+str(low)+" high"+str(high))
    #print(newLightPow)
    
  check = True
  for i in range(0, N):
    if (i > 0):
      newLightPow[i] += newLightPow[i-1]
    if (newLightPow[i] < N):
      check = False
  lightPow = newLightPow
  if (check):
    break

print(*lightPow[:-1])