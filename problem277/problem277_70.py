#!/usr/bin/env python3




def main():
    h,w,k = map(int, input().split())
    s = [input() for i in range(h)]
    l = [[0]*w for i in range(h)]
    
    from collections import deque

    d = deque()
    c = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                d.append([i, j])
                l[i][j] = c
                c += 1
    

    while len(d) > 0:
        x,y = d.pop()
        c = l[x][y]
        l[x][y] = c
        f1 = True
        f2 = True
        for i in range(1,w):
            if y+i < w and l[x][y+i] == 0 and s[x][y+i] != '#' and f1:
                l[x][y+i] = c
            else:
                f1 = False

            if 0 <= y-i and l[x][y-i] == 0 and s[x][y-i] != '#' and f2:
                l[x][y-i] = c
            else:
                f2 = False


    for i in range(h):
        if all(l[i]) == 0:
            k1 = 1
            while 0 < i+k1 < h and all(l[i+k1]) == 0:
                k1 += 1
            # print("test: ", i, k1)
            if i+k1 < h:
                for j in range(i, i+k1):
                    for r in range(w):
                        l[j][r] = l[i+k1][r]

    for i in range(h-1, -1, -1):
        if all(l[i]) == 0:
            k1 = 1
            while 0 < i-k1 < h and all(l[i-k1]) == 0:
                k1 += 1
            # print("test: ", i, k1)
            if 0 <= i-k1 < h:
                for j in range(i, i-k1, -1):
                    for r in range(w):
                        l[j][r] = l[i-k1][r]
    

                    
    for i in range(h):
        print(' '.join(map(str, l[i])))
            

    

if __name__ == '__main__':
    main()
