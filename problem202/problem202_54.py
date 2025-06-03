n,a,b = map(int,input().split())
result = n // (a + b) * a
result += min(n % (a + b),a)
print(result)