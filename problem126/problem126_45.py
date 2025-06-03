def a():
    l = map(int, input().split())
    res = [i + 1 for i, v in enumerate(l) if v == 0]
    if len(res) > 1:
        r = res[-1]
    else:
        r = res[0]
    print(r)


if __name__ == "__main__":
    a()
