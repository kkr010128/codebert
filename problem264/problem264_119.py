def mainFunc():
    m1, d1 = list(map(int, list(input().split(" "))))
    m2, d2 = list(map(int, list(input().split(" "))))

    ans = '1' if m1 != m2 else '0'
    print(ans)
mainFunc()