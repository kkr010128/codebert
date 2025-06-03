def main():
    input()
    a = set(input().split())
    input()
    b = set(input().split())
    print(len(a.intersection(b)))


if __name__ == "__main__":
    import os
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            fd = os.open("input.txt", os.O_RDONLY)
            os.dup2(fd, sys.stdin.fileno())
            main()
    else:
        main()