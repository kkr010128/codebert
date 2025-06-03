import numpy as np
X = int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
div = make_divisors(X)
for i in range(len(div)):
    x = div[i]
    z = x**4 - X/x
    if z%5 == 0:
        s = z / 5
        if x**4 - 4*s >=0:
            y1 =( -x**2 + np.sqrt(x**4 - 4 * s)) / 2
            y2 =( -x**2 - np.sqrt(x**4 - 4 * s)) / 2 
            B1 = (-x + np.sqrt(x**2 + 4*y1))/2
            if B1.is_integer():
                B = B1
                A = B + x
                break
            B12 = (-x + np.sqrt(x**2 + 4*y2))/2
            if B12.is_integer():
                B = B12
                A = B + x
                break
            B2 = (-x - np.sqrt(x**2 + 4*y1))/2
            if B2.is_integer():
                B = B2
                A = B + x
                break
            B21 = (-x - np.sqrt(x**2 + 4*y2))/2
            if B21.is_integer():
                B = B21
                A = B + x
                break
print(int(A),int(B))
