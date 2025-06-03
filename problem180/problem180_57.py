N, K = map(int, input().split())

def f(x):
    return( N-x*K )

def test(x):
    return( f(x) >= 0 )

left = - 1        # return = right = (取り得る値の最小値) の可能性を排除しないために、-1 が必要
right = 10**18

while right - left > 1:             # 最終的に (right, left, mid) = (最小値, 最小値 - 1, 最小値 - 1) に収束するため、差が 1 になったときに終了すればよい
    mid = (left+right)//2
    if test(mid):
        left = mid
    else:
        right = mid
print(min(abs(N-left*K), abs(N-right*K)))