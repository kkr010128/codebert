N, M = map(int, input().split(" "))
 
a = list(set(map(int, input().split(" "))))
g = a.copy()
 
while not any(x%2 for x in g): g = [i //2 for i in g]
 
if not all(x%2 for x in g): print(0); exit(0)
 
def gcd(a, b):
 
    while b:
 
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return a * b // gcd(a, b)
 
 
tot = 1
 
for x in a: tot = lcm(tot, x//2)
print((M//tot+1)//2)