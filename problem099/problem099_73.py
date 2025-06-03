def solve():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    left = 0
    right = 10 ** 9
    while right - left > 1:
        mid = (right+left) // 2
        cnt = 0
        for a in A:
            cnt += (a-1) // mid
        
        if cnt <= K:
            right = mid
        else:
            left = mid

    print(right)
    
if __name__ == '__main__':
    solve()
