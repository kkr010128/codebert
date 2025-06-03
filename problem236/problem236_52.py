import math


H,W,N = [int(input()) for i in range(3)]
 
print(min(math.ceil(N/H),math.ceil(N/W)))