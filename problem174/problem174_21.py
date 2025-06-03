def N():
    return int(input())
def L():
    return list(map(int,input()))
def NL(n):
    return [list(map(int,input())) for _ in range(n)]
import math
k = N() + 1
sum = 0
for i in range(1,k):
    for j in range(1,k):
        for l in range(1,k):
            #print(sum)
            sum += math.gcd(math.gcd(i,j),l)
print(sum)
