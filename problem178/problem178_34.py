def main():
    s = list(map(int,input().strip().split()))
    tmp = s[0]
    s[0] = s[1]
    s[1] = tmp

    tmp = s[0]
    s[0] = s[2]
    s[2] = tmp

    print("{} {} {} ".format(s[0],s[1],s[2]))
main()
