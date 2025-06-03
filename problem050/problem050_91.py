while True:
    h, w = [int(i) for i in input().split(' ')]
    if h ==0 and w ==0:
        break
    for i in range(h):
        row = ''
        for j in range(w):
            if i == 0 or i == h - 1:
                row = row + '#'
            else:
                if j == 0 or j == w -1:
                    row = row + '#'
                else:
                    row = row + '.'
        print(row)
    print('')
