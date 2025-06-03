def padd(x, ans):
    if x==1:
        ans += 300000
    elif x==2:
        ans += 200000
    elif x==3:
        ans += 100000
    return ans

def main():
    x, y = map(int, input().split())
    ans = 400000 if x==1 and y==1 else 0
    ans = padd(x, ans)
    ans = padd(y, ans)
    print(ans)

main()