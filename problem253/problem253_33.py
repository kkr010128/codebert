n, a, b = map(int, input().split())
print((b-a)//2 + min(a-1,n-b) + 1 if (b-a)%2 else (b-a)//2)