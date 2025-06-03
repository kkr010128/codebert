import bisect
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = list(input())
    Q = int(input())
    set_dic = {}

    for i, s in enumerate(S):
        if s not in set_dic:
            set_dic[s] = [i+1]
        else:
            bisect.insort_left(set_dic[s], i+1)

    anslist = []

    for _ in range(Q):
        query1, query2, query3 = input().split()
        if query1 == "1":
            i = int(query2)
            c = query3
            cap = S[i-1]
            if cap == c:
                continue
            set_dic[cap].remove(i)
            if c not in set_dic:
                set_dic[c] = [i]
            else:
                bisect.insort_left(set_dic[c], i)
            S[i-1] = c
        else:
            l = int(query2)
            r = int(query3)
            ansset = set()
            ans = 0
            for eachlist in set_dic.values():
                li = bisect.bisect_left(eachlist, l)
                ri = bisect.bisect_right(eachlist, r)
                if li != ri:
                    ans += 1
            anslist.append(ans)

    for i in anslist:
        print(i)

if __name__ == '__main__':
    solve()