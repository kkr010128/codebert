ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y
n,k = inm()
p = inl()
p = sorted(p)
print(sum(p[:k]))
