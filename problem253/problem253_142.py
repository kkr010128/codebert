n,a,b = map(int,input().split())
if (a % 2 + b % 2) % 2 == 0:
    print(abs(a - b) // 2)
    exit(0)

if n - b < a - 1:
    p = n - b + 1
    a += n - b
    b = n
    print(abs(a - b) // 2 + p)
else:
    p = a - 1 + 1
    b -= a - 1
    a = 1
    print(abs(a - b) // 2 + p)