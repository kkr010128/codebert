n, m = map(int, input().split())
a = list (map(int, input().split()))

b = sum(a)

if n >= b:
    print( n - b )

if n < b:
    print( -1 )