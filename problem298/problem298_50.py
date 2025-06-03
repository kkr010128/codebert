# B - Roller Coaster
def main():
    cnt = 0
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    print(sum([cnt+1 for v in h if v >= k]))

if __name__ ==  "__main__":
    main()