N, M = map(int, input().split())

A = list(set(map(int, input().split(" "))))
G = A.copy()
 
while not any(x % 2 for x in G):
    G = [i // 2 for i in G]
 
if not all(x % 2 for x in G):
    print(0)
    exit(0)
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
total = 1

for x in A:
    total = lcm(total, x // 2)

print((M // total + 1) // 2)
