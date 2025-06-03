def resolve():
    N = int(input())
    XY = []
    for i in range(N):
        A = int(input())
        xy = [list(map(int, input().split())) for _ in range(A)]
        XY.append(xy)
    
    ans = 0
    for _bits in range(1<<N):
        bits = list(map(int, bin(_bits)[2:].zfill(N)))
        unmatch = False
        for i in range(N):
            if bits[i] == 0:
                continue
            for x, y in XY[i]:
                if bits[x-1] != y:
                    unmatch = True
                    break
            if unmatch:
                break
        else:
            ans = max(ans, bin(_bits).count('1'))
    print(ans)



if '__main__' == __name__:
    resolve()