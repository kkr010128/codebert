import math
 
w = 0
k = int(input())
for i in range(1, k+1):
    for j in range(1, k+1):
        m = math.gcd(i, j)
        for l in range(1, k+1):
            w += math.gcd(m, l)
print(w)