import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    p = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    print(7 - p.index(S))


if __name__ == '__main__':
    main()
