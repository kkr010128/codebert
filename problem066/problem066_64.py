while True:
    d = input()
    if d == '-':
        break
    h = int(input())
    rotate = 0
    for i in range(h):
        rotate += int(input())
    move = rotate % len(d)
    print(d[move:] + d[:move])

