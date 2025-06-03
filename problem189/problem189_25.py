N, M = map(int, input().split())
totalN = 1/2*(N-1)*N
totalM = 1/2*(M-1)*M
import math

print(math.floor(totalN + totalM))
