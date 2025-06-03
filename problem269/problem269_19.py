def main():
    # input
    import math
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    x = (a1-b1)*t1
    y = (a2-b2)*t2
    diff = x+y

    if x == -y:
        print("infinity")
        return
    elif x*y>0 or abs(x)>abs(y):
        print(0)
        return

    x = abs(x)
    diff = abs(diff)
    ans = x//diff
    remainder = x%diff
    if remainder==0:
        print(ans*2)
    else:
        print(ans*2+1)

    # calc

if __name__ == '__main__':
    main()
