def main():
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    circle = a[0] * t[0] + a[1] * t[1] - b[0] * t[0] - b[1] * t[1]
    if circle == 0:
        print('infinity')
        return
    d = [0, 0]
    cd = 0
    ans = -1
    for i in range(2):
        d[i] = cd + a[i] * t[i] - b[i] * t[i]
        if cd * d[i] <= 0:
            ans += 1
        cd = d[i]
    if ans == 0:
        print(0)
        return
    if circle < 0:
        if d[0] > 0:
            ans += d[0] // -circle * 2
            if d[0] % (-circle) == 0:
                ans -= 1
        elif d[1] > 0:
            ans += d[1] // -circle * 2
            if d[1] % (-circle) == 0:
                ans -= 1
    else:
        if d[0] < 0:
            ans += -d[0] // circle * 2
            if -d[0] % (circle) == 0:
                ans -= 1
        elif d[1] < 0:
            ans += -d[1] // circle * 2
            if -d[1] % (circle) == 0:
                ans -= 1
    print(ans)
main()