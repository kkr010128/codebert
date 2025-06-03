import sys
input = sys.stdin.readline

def main():
    s = input().strip()
    print("ABC" if s[1] == "R" else "ARC")


if __name__ == "__main__":
    main()