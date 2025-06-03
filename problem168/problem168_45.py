n, m = map(int,input().split())
a = list(map(int,input().split()))
b = 0

for i in a:
    b = b + i

if n >= b:
    print(n - b)
if n < b:
    print( -1 )