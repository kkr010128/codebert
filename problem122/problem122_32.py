def main():
    n = int(input())
    a = list(map(int,input().split()))
    d= {}
    for i in range(n):
        if d.get(a[i])==None:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    s = sum(a)
    q = int(input())
    for i in range(q):
        b,c = map(int,input().split())
        if d.get(b)==None:
            print(s)
        else:
            s += (c-b)*d[b]
            if d.get(c)==None:
                d[c] = d[b]
            else:
                d[c] += d[b]
            d[b] = 0
            print(s)

if __name__ == "__main__":
    main()
