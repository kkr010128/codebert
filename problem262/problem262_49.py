from collections import deque


def solve():
    N = int(input())
    XY= [[]]
    for _ in range(N):
        A = int(input())
        xylist = []
        for __ in range(A):
            x, y = map(int, input().split())
            xylist.append([x,y])
        XY.append(xylist)
        ans = 0
    for bit in range(2 ** N):
        honestset = set()
        unhonestset = set()
        for i in range(N):
            if ((bit >> i) & 1) == 1:
                honestset.add(i+1)
            else:
                unhonestset.add(i+1)

        before = 100
        before_un = 100
        while (before != len(honestset) or before_un != len(unhonestset)):
            before = len(honestset)
            before_un = len(unhonestset)
            tmp = list(honestset)
            for x in tmp:
                for xin, yin in XY[x]:
                    if yin == 1:
                        honestset.add(xin)
                    else:
                        unhonestset.add(xin)
        if len(honestset & unhonestset) == 0:
            ans = len(honestset) if ans < len(honestset) else ans

    print(ans)


if __name__ == '__main__':
    solve()
