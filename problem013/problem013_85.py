def main():
    N = int(input())
    price = [int(input()) for i in range(N)]
    minv = float("inf")
    maxv = -float("inf")
    for p in price:
        maxv = max(maxv, p-minv)
        minv = min(minv, p)
    print(maxv)



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