import math
k = int(input())
sum_gcd = 0

for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):

            sum_gcd += math.gcd(math.gcd(a,b) , c)

print(sum_gcd)