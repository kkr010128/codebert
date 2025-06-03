import sys


# input = sys.stdin.readline

def main():
    A,B = map(int,input().split())
    if A//10 +B//10 >0:
        print(-1)
    else:
        print(A*B)


if __name__ == "__main__":
    main()