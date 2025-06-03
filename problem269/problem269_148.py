def main():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    x, y = (a1-b1)*t1, (a2-b2)*t2
    if x//abs(x) == y//abs(y):
        print(0)
    else:
        if abs(x) == abs(y):
            print("infinity")
        else:
            x, y = abs(x), abs(y)
            if y < x:
                print(0)
            else:
                if x%(y-x) != 0:
                    print((x+(y-x)-1)//(y-x)*2-1)
                else:
                    print(x//(y-x)*2)

if __name__ == "__main__":
    main()