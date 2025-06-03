n, a, b = map(int, input().split())
ret = 0
ret += a*(n//(a+b))
rem = n%(a+b)
ret += min(rem, a)
print(ret)