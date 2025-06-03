from math import ceil


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(Min):
        kill = 0
        for a in A:
            kill += (ceil(a/Min)-1)
        return kill <= K

    l = 0
    r = 1000000000

    while r-l > 1:
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)
        


if __name__ == '__main__':
    main()