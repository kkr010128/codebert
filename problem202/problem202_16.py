n,a,b = map(int,input().split())
ab = a + b
m = n // ab
n %= ab
print(m*a+min(n,a))