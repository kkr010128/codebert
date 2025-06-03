def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for _ in range(n):
        ca = [int(v) for v in input().split()]
        c.append(ca[0])
        a.append(ca[1:])
    
    INTHIGH = 1<<32
    pricemin = INTHIGH
    for i in range(1<<n):
        sm = [0]*m
        sc = 0
        for j in range(n):
            if i & 1<<j:
                sc += c[j]
                for k in range(m):
                    sm[k] += a[j][k]
                if min(sm)>=x:
                    pricemin = min(pricemin, sc)
                    break

    print(pricemin if pricemin<INTHIGH else -1) 

main()