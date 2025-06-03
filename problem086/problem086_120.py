N,X,T = map(int,input().split())
# N個のたこやき作る, T分ずつ、最大X個同時
import math
print(int(math.ceil(N / X) * T))