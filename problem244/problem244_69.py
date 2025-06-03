import sys


# input = sys.stdin.readline

def main():
    K, X= map(int,input().split())
    if X<= K*500:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()