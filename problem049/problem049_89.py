while True:
    h, w = [int(i) for i in input().split(' ')]
    if h ==0 and w ==0:
        break
    for i in range(h):
        row = ''
        for j in range(w):
            row = row + '#'
        print(row)
    print('')
