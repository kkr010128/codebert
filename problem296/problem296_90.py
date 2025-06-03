#!python3

iim = lambda: map(int, input().rstrip().split())

def resolve():
    S = input()
    K = int(input())

    ls = len(S)

    if ls == 1:
        print(K//2)
        return

    if ls == 2:
        print(0 if S[0] != S[1] else K)
        return

    if S[0] == S[-1]:
        c0 = S[0]
        for i in range(1, ls):
            if c0 != S[i]:
                break
        else:
            print(ls*K//2)
            return
        i0 = i
    else:
        i = i0 = 0

    ans = 0
    c0 , cn = "", 0
    for i in range(i, ls):
        c1 = S[i]
        if c1 == c0:
            cn += 1
        else:
            if cn > 1:
                ans += cn // 2
            cn = 1
            c0 = c1

    if i0 == 0:
        if cn > 1:
            ans += cn // 2
        ans *= K
    else:
        ans = ans * K + ((i0+cn)//2) * (K-1) + i0//2 + cn//2


    print(ans)

if __name__ == "__main__":
    resolve()
