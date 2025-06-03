def main():
    import itertools
    n = int(input())
    test = []
    for i in range(n):
        a = int(input())
        t = []
        for j in range(a):
            x,y = map(int,input().split())
            t.append([x,y])
        test.append(t)
    stats = ((0,1) for i in range(n))
    ans = 0
    for k in itertools.product(*stats):
        tf = [-1 for i in range(n)]
        flg = 0
        for i in range(len(k)):
            if k[i]==1:
                for t in test[i]:
                    if tf[t[0]-1]==-1:
                        tf[t[0]-1] = t[1]
                    else:
                        if tf[t[0]-1] != t[1]:
                            flg = 1
                            break
        for i in range(len(k)):
            if tf[i] != -1:
                if tf[i] != k[i]:
                    flg = 1
                    break
        if flg == 0:
            if ans < sum(k):
                ans = sum(k)
    print(ans)

if __name__ == "__main__":
    main()
