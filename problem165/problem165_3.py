import sys
input = sys.stdin.readline

def main():
    N = int(input())
    S = set([input().rstrip() for _ in range(N)])
    print(len(S))


if __name__ == '__main__':
    main()
