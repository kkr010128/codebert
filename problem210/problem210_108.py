def main():
    global s,ide_ele,num,seg
    n = int(input())
    s = list(input())
    for i in range(n):
        s[i] = ord(s[i])-97
    ide_ele = 0
    num = 2**(n-1).bit_length()
    seg = [[ide_ele for _ in range(2*num)] for _ in range(26)]
    for i in range(n):
        seg[s[i]][i+num-1] = 1
    for a in range(26):
        for i in range(num-2,-1,-1) :
            seg[a][i] = max(seg[a][2*i+1],seg[a][2*i+2])
    q = int(input())
    for _ in range(q):
        QUERY = list(input().split())
        QUERY[0], QUERY[1] = int(QUERY[0]), int(QUERY[1])
        if QUERY[0] == 1:
            x = ord(QUERY[2])-97
            k = QUERY[1]-1
            pre = s[k]
            s[k] = x
            k += num-1
            seg[pre][k] = 0
            seg[x][k] = 1
            while k:
                k = (k-1)//2
                seg[pre][k] = max(seg[pre][k*2+1],seg[pre][k*2+2])
                seg[x][k] = max(seg[x][k*2+1],seg[x][k*2+2])
        if QUERY[0] == 2:
            P, Q = QUERY[1]-1, int(QUERY[2])
            if Q <= P:
                print(ide_ele)
                break
            P += num-1
            Q += num-2
            ans = ide_ele
            for i in range(26):
                res = ide_ele
                p,q = P,Q
                while q-p > 1:
                    if p&1 == 0:
                        res = max(res,seg[i][p])
                    if q&1 == 1:
                        res = max(res,seg[i][q])
                        q -= 1
                    p = p//2
                    q = (q-1)//2
                if p == q:
                    res = max(res,seg[i][p])
                else:
                    res = max(max(res,seg[i][p]),seg[i][q])
                ans += res
            print(ans)

if __name__ == "__main__":
    main()