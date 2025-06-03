def main():
    S = input()
    K = int(input())
    l = []
    t = 1
    m = S[0]
    if len(S) == 1:
        print(K//2)
        return
    if len(S) == 2:
        if S[0] == S[1]:
            print(K)
            return
        else:
            print(0)
            return
    if len(S) == 3:
        if S[0] == S[1] == S[2]:
            print(3*K//2)
            return
        elif S[0] == S[1] or S[1] == S[2]:
            print(K)
            return
        elif S[0] == S[2]:
            print(K-1)
            return
        else:
            print(0)
            return
    for v in S[1:]:
        if v == m:
            t += 1
        elif t != 1:
            l.append(t)
            t = 1
        m = v
    if t != 1:
        l.append(t)
    ls = 0
    lsm = 0
    lsu = 0
    if S[0] == S[-1]:
        if len(l) == 1 and l[0] == len(S):
            print(l[0] * K//2)
            return
        elif len(l) == 1:
            print(((l[0] + 1)//2) *(K-1) + (l[0] // 2))
            return
        if S[0] == S[1] == S[-2]:
            ls = l[-1] + l[0]
            lsm = l[0]
            lsu = l[-1]
            l = l[1:-1]
        elif S[-1] == S[-2]:
            ls = l[-1] + 1
            lsu = l[-1]
            l = l[:-1]
        elif S[0] == S[1]:
            ls = l[0] + 1
            lsm = l[0]
            l = l[1:]
        else:
            ls = 2
    r = 0
    for i in l:
        r += i // 2
    r *= K
    r += (K-1) * (ls // 2)
    r += (lsm  // 2) + (lsu // 2)
    print(r)
main()
