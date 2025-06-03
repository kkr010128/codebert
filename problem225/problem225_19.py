import sys
input = sys.stdin.readline


def main():
    H, A = map(int, input().split())
    answer = 0
    while H > 0:
        H -= A
        answer += 1
    print(answer)


if __name__ == '__main__':
    main()
