import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
X = int(readline())
def make_divisors(n):
    lower_divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
        i += 1
    return lower_divisors 

A = make_divisors(X)
for a in A:
    for b in range(10**3,-(10**3),-1):
        Y = X // a
        if ((b+a)**4 + b*(b+a)**3 + b**2*(b+a)**2 + b**3*(b+a) + b**4) == Y:
            print(b+a,b)
            sys.exit()