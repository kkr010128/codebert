if __name__ == '__main__':
    import sys
    input = sys.stdin.readline



    n, k = map(int, input().split())

    ww = [0]*n
    for i in range(n):
        ww[i] = int(input())

    max_w = 10000

    max_p = max_w*n
    min_p = 0


    def number_of_track(p):
        ans = 1
        sum_w = 0
        for w in ww:
            if w > p:
                return n+1
            if sum_w + w > p:
                ans += 1
                sum_w = w
            else:
                sum_w += w
        return ans

    while min_p != max_p:
        mid = (max_p + min_p)//2
        if number_of_track(mid) <= k:
            max_p = mid
        else:
            min_p = mid+1
    print(max_p)

