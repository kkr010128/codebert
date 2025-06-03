from collections import defaultdict

def gcd(x, y):
    r = x % y
    while r:
        x, y, r = y, r, y%r
    return y
    
def main():
    n = int(input())
    al = defaultdict(lambda: 0)
    All = 0
    mod = 1000000007
    goods = dict()
    for i in range(n):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            All += 1
        elif b == 0:
            al["inf"] += 1
            goods["inf"] = "0"
        elif a == 0:
            al["0"] += 1
            goods["0"] = "inf"
        else:
            g = gcd(b, a)
            a_key = f"{a//g},{b//g}"
            if b//g < 0:
                good = f"{-b//g},{a//g}"
            else:
                good = f"{b//g},{-a//g}"
            goods[a_key] = good
            al[a_key] += 1
    ans = 1
    al = dict(al)
    done = set()
    ok = 0
    for k, v in al.items():
        if k in done:
            continue
        num = al.get(goods[k])
        done.add(goods[k])
        if num:
            ans *= pow(2, num, mod)+pow(2, v, mod)-1
            ans %= mod
        else:
            ok += v
    ans *= pow(2, ok, mod)
    ans += All - 1
    ans %= mod
    print(ans)
        
        
            
    

if __name__ == "__main__":
    main()