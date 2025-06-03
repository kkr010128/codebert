def main():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())

    if v <= w:
        print("NO")
    else:
        if abs(a - b) <= t * (v - w):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
