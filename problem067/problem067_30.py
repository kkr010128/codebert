#
# 9c
#

def main():
    T = H = 0
    n = int(input())
    for i in range(n):
        t, h = input().split()
        if t > h:
            T += 3
        elif t < h:
            H += 3
        else:
            T += 1
            H += 1

    print(f"{T} {H}")


if __name__ == '__main__':
    main()

