from sys import stdin

while True:
    h, w = (int(n) for n in stdin.readline().rstrip().split())

    if h == w == 0:
        break

    for cnt in range(h):
        print(('#.' * ((w + 2) // 2))[cnt % 2: w + cnt % 2])

    print()

