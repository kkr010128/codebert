n,a,b = map(int,input().split())

if (a - b) % 2 == 0:
    print(min(abs(a-b) // 2, max(a-1, b-1), max(n-a, n-b)))
else:
    print(min(max(a-1, b-1), max(n-a, n-b), (a+b-1)//2, (2 * n - a - b + 1)//2))
