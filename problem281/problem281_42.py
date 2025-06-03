P = 10**9 + 7
X, Y = map(int, input().split())

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
        res %= P
    return res

if (2*X-Y)%3 == 0 and (-X+2*Y)%3 == 0 and 2*X-Y >= 0 and -X+2*Y >= 0:
    a = (-X+2*Y)//3
    b = (2*X-Y)//3
    print((factorial(a+b)*pow(factorial(a), P-2, P)*pow(factorial(b), P-2, P))%P)
else:
    print(0)