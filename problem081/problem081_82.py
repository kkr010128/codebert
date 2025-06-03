def main():
    d, t, s = map(int, input().split())
    if d <= (t*s):
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()
