def main():
    a, b, c, d = map(int, input().split())
    if a*b > 0 and c*d > 0 and a*c < 0:
        print(max(a*d, b*c))
    else:
        print(max(a*c, b*d, 0))

if __name__ == "__main__":
    main()