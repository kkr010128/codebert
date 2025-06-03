def solve():
    N = int(input())
    XLs = [list(map(int, input().split())) for _ in range(N)]
    XLs.sort(key = lambda x:(x[0],-1*x[1]))
    interval = (XLs[0][0]-XLs[0][1],XLs[0][0]+XLs[0][1])
    ret = 0
    for XL in XLs[1:]:
        interval_ = (XL[0]-XL[1], XL[0]+XL[1])
        if interval_[0] < interval[1]:
            interval = (max(interval[0], interval_[0]),min(interval[1], interval_[1]))
            ret += 1
        else:
            interval = interval_
            
    print(N-ret)
    
solve()