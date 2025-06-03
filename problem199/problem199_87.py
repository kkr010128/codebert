def main():
    s = input()
    ok = False
    hi = ""
    for _ in range(5):
        hi += "hi"
        if s == hi:
            ok = True
    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()