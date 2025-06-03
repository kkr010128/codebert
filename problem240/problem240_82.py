# input here
_INPUT = """\
2 5
1 WA
1 AC
2 WA
2 AC
2 WA
2 AC
"""

def main():
    n, m= map(int, input().split())
    ps = [list(map(str,input().split())) for _ in range(m)]

    str_l = ["WA"]*n
    int_l = [0]*n
    num = 0
    ac = 0

    for pp, s in ps:
        p = int(pp)-1
        if s == "AC":
            str_l[p] = "AC"
        else:
            if str_l[p] != "AC":
                int_l[p] += 1

    for i in range(n):
        if str_l[i] == "AC":
            num += int_l[i]
            ac += 1

    print(ac,num)
    # n, m = map(int, input().split())

    # seikai = [False] * n
    # matigai = [0] * n

    # for i in range(m):
    #     p,q = map(str, input().split())
    #     p = int(p)-1

    #     if q == "AC":
    #         seikai[p] = True
    #     else:
    #         if seikai[p] != True:
    #             matigai[p] += 1


    # correct = seikai.count(True)
    # mistake = sum(matigai)
    # print(correct, mistake)
            
if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools
    from collections import deque

    # sys.stdin = io.StringIO(_INPUT)
    main()