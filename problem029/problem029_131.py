import math
A = list(map(float, input().split()))

ans = math.sqrt((A[0]-A[2])**2 + (A[1]-A[3])**2)
print(ans)
