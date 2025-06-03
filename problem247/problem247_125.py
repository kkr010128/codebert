from functools import reduce

n, m = map(int, input().split())
a = list(map(int, input().split()))

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

def count(n):
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    return cnt

A = [count(i) for i in a]

if len(set(A)) != 1:
    print(0)
    exit()

aa = [i // 2 for i in a]
LCM = reduce(lcm, aa)

res = m // LCM
if res % 2 == 0:
    print(res // 2)
else:
    print(res // 2 + 1)
