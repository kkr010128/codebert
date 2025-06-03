def main():
    x = int(input())
    a, b = 1, 0

    while True:
        for b in reversed(range(-a + 1, a)):
            # print(a, b)
            q = a**5 - b**5
            if q == x:
                print(f'{a} {b}')
                return
        a += 1

main()