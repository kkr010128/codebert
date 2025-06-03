import numpy as np 

s_ = np.array(input().split())
s = [int(i) for i in s_]
N,X,T =s[0],s[1],s[2]
n = N//X
if N % X != 0:
  n += 1
out = n * T
print(out)
