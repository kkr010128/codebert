def award(x):
    return max(0, 4*(10**5) - x*(10**5))

x,y = map(int,input().split())

ans  = award(x)
ans += award(y)

if x == 1 and y == 1:
    ans += 4*(10**5)

print(ans)