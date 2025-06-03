from math import ceil
def solve():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    left = 0
    right = 10 ** 9
    while (right - left) > 1:
        x = (left+right) // 2
        cnt = 0
        for a in A:
            cnt += (a-1) // x
        
        if cnt <= K:
            right = x
        else:
            left = x
    
    print(right)
    
if __name__ == '__main__':
    solve()
