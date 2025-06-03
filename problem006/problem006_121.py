import math
n=int(input())
S=100
for i in range(n):
    S=S+0.05*S
    S=math.ceil(S)
print(S*1000)

