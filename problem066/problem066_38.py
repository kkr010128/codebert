#
# 9b
#

def main():
    while True:
        c = input()
        if c == "-":
            break
        m = int(input())
        for i in range(m):
            h = int(input())
            c = c[h:] + c[0:h]
        print(c)


if __name__ == '__main__':
    main()

