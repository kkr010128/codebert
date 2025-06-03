def linearSearch(S, T):
    cnt = 0
    for e in T:
        if e in S:
            cnt += 1
    return cnt


def main():
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))

    print(linearSearch(s, t))

if __name__ == "__main__":
    main()