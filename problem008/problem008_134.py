def srch(u, cnt, Dst, Fst, Lst):
    S = [u]
    Fst[u] = cnt
    while(len(S) > 0):
        cnt += 1
        u = S.pop()
        if Dst[u] is not None and len(Dst[u]) > 0:
            while(len(Dst[u])):
                u1 = Dst[u].pop()
                if Fst[u1] == 0:
                    S.append(u)
                    S.append(u1)
                    Fst[u1] = cnt
                    break
                else:
                    Lst[u] = cnt
        else:
            Lst[u] = cnt
    return cnt + 1

def main():
    num = int(input())
    Dst = [None for i in range(num + 1)]
    Fst = [0] * (num + 1)
    Lst = Fst[:]

    for n in range(1, num+1):
        a = list(map(int,input().split()))
        u = a[0]
        if a[1] > 0:
            Dst[u] = a[2:]
            Dst[u].reverse()

    cnt = 1
    for i in range(1,num):
        if Fst[i] == 0:
            cnt = srch(i, cnt, Dst, Fst, Lst)

    for n in range(1, num+1):
        print("{} {} {}".format(n,Fst[n],Lst[n]))

if __name__ == '__main__':
    main()