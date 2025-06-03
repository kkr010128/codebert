import math
def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans*= i
    return ans
def comb(n, c):
    return fact(n)//(fact(n-c)*c)

x = int(input())
a = 0
b = 0
done = False
for f in range(-300, 300):
    for l in range(-300, 300):
        if((f**5)-(l**5)==x):
            a = f
            b = l
            done = True
            break
    if(done):
        break
print(a,b)
