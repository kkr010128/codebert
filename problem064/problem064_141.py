#
# 8d
#


def main():
    s = input()
    p = input()

    ret = ""
    s = s + s
    if p in s:
        ret = "Yes"
    else:
        ret = "No"
    print(ret)


if __name__ == '__main__':
    main()
