def main():
    S, W = map(int, input().split())
    un = "un" if W >= S else ""
    print(un + "safe")


if __name__ == "__main__":
    main()
