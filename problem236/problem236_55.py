import math
H = int(input())
W = int(input())
N = int(input())

Big = W if W > H else H

print(math.ceil(N / Big))