def main():
    n = int(input())
    if n == 0:
        print("Yes")
        return
    slup = []
    sldown = []
    for i in range(n):
        height, mi = 0, 0
        for si in input():
            if si == "(":
                height += 1
            else:
                height -= 1
                mi = min(mi, height)
        if height >= 0:
            slup.append([mi, height])
        else:
            sldown.append([mi-height, -height])

    slup.sort(key = lambda x: -x[0])
    sldown.sort(key = lambda x: -x[0])
    if sum([si[1] for si in slup]) + sum([-si[1] for si in sldown]):
        print("No")
        return
    h = 0
    for si in slup:
        if h+si[0] < 0:
            print("No")
            return
        h += si[1]
    h = 0
    for si in sldown:
        if h+si[0] < 0:
            print("No")
            return
        h += si[1]
    print("Yes")
        

if __name__ == "__main__":
    main()