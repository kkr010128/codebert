def main():
    ss = input()
    if ss[-1] == "s":
        ans = ss + "es"
    else:
        ans = ss + "s"
    print(ans)


if __name__ == "__main__":
    main()
