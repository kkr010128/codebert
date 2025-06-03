import fractions

def is_lcm(X, Y):
    return X*Y // fractions.gcd(X, Y)

N, M = map(int, input().split())

print(is_lcm(N, M))