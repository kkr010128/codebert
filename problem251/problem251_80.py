from itertools import groupby
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(k):
        x = i
        li = []
        while x < n:
            li.append(t[x])
            x += k
        for key, value in groupby(li):
            if key=='r':
                a=p
            elif key=='s':
                a=r
            else:
                a=s

            ans += ((len(list(value))+1)//2)*a
    print(ans)


if __name__ == '__main__':
    main()