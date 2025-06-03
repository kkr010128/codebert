x, y = map(int, input().split())

ans = 0

def calc(z):
    ans = 0
    if z == 1:
        ans += 300000
    elif z == 2:
        ans += 200000
    elif z == 3:
        ans += 100000
    
    return ans

if x == 1 and y == 1:
    ans += 400000

print(ans+calc(x)+calc(y))