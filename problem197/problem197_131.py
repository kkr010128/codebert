
def main():
    a, b, c = map(int, input().split())
    if 4*a*b < pow(c - (a + b), 2):
        ans = 'Yes'
    else:
        ans = 'No'
    if c - (a + b) <= 0:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
