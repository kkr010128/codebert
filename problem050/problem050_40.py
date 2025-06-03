while True:
    h, w = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    else:
        result = list()
        for i in range(h):
            result.append(['#' for j in range(w)])
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                result[i][j] = '.'
        for i in result:
            print("".join(j for j in i))
        print("")