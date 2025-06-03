def main():
    S = input()

    lst = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    ans = 7 - lst.index(S)

    print(ans)


if __name__ == "__main__":
    main()
