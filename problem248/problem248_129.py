import sys
input = sys.stdin.readline

INF = float('inf')


def main():
    S, T = map(str, input().split())
    print(T + S)


if __name__ == '__main__':
    main()
