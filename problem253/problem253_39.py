n, a, b = map(int,input().split())
if a % 2 == b % 2:
    print((b-a)//2)
else:
    ans = min(n-b, a-1) + 1 + (b-a-1)//2
    print(ans)