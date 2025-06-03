n,k = [int(x) for x in input().split()]
a = n // k
n -= a * k
print(min(n,abs(n-k)))