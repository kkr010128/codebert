ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y

a,b = input().split()
b = b[:-3] + b[-2:]
ans = int(a) * int(b)
ans = ans // 100
print(ans)
