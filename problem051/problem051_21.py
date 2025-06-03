# coding : utf-8
lst = []
while True:
    h, w = map(int, input().split())
    lst.append([h, w])
    if h == 0 and w == 0:
        break
for l in lst:
    H = l[0]
    W = l[1]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                print ('#', end = '')
            else:
                print ('.', end = '')
        print ('')
    if i == H-1:
        print ('')

