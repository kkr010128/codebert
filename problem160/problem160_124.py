def main():
    import itertools
    n,m,q = map(int,input().split())
    Q = []
    for i in range(q):
        Q.append(list(map(int,input().split())))
    cmb = [i for i in range(1,m+1)]
    ans = 0
    for que in itertools.combinations_with_replacement(cmb,n):
        m = 0
        for i in range(q):
            [a,b,c,d] = Q[i]
            if que[b-1]-que[a-1]==c:
                m += d
        if m>ans:
            ans = m
    print(ans)

if __name__ == "__main__":
    main()
