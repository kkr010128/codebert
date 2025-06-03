import sys


# input = sys.stdin.readline

def main():
    N = int(input())
    S = input()
    if N %2 ==1:
        print("No")
        exit()
    else:
        half = int(N/2)
        if S[0:half] *2== S:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()