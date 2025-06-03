#
# 9d
#

def main():
    s = input()
    q = int(input())
    for i in range(q):
        l = list(input().split())
        a = int(l[1])
        b = int(l[2])
        if l[0] == "print":
            print(s[a:b+1])
        elif l[0] == "reverse":
            s = s[0:a] + s[a:b+1:][::-1] + s[b+1:]
        elif l[0] == "replace":
            s = s[0:a] + l[3] + s[b+1:]
        else:
            pass


if __name__ == '__main__':
    main()
