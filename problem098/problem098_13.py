if __name__ == '__main__':

    n = int(input())
    A = list(input())

    white = A.count("W")
    red   = A.count("R")

    #最終形を作る
    B = sorted(A)

    #現在の形と最終形との比較をする
    a = b = 0
    for w,r in zip(A,B):
        if w != r:
            if w == "W":
                a += 1
            else:
                b += 1

    #結果
    com = min(a,b)
    bg = max(a,b)
    dif = bg - com
    ans = com + dif
    print(ans)
