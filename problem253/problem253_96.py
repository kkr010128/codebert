n,a,b = map(int, input().split())

ans = (b-a)//2
if (b-a)%2 == 1:
    ans += 1 + min(a-1,n-b)
print(ans)