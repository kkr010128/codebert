a,b = map(int,input().split())

ans = 0

if a - (2 * b) > 0:
    ans = a - (2 * b)
    
print(ans)