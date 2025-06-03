if __name__ == '__main__':
    from sys import stdin

    while True:
        m, f, r = (int(n) for n in stdin.readline().rstrip().split())

        if m == f == r == -1:
            break

        s = m + f
        result = "F" if m == -1 or f == -1 \
            else "A" if 80 <= s \
            else "B" if 65 <= s \
            else "C" if 50 <= s or 50 <= r \
            else "D" if 30 <= s \
            else "F"

        print(result)

