"""ABC174E diff: 1158
"""

N,K=map(int,input().split())
A=list(map(int, input().split()))

if K == 0:
    print(max(A))
    exit()

def f(x):
    """
    K回以内のカットで全ての丸太の長さをX以下にできるか？
    X: int
    Return: bool
    """
    cnt = 0
    for a in A:
        if a % x == 0:
            cnt += a//x - 1
        else:
            cnt += a//x
    
    if cnt <= K:
        return True
    else:
        return False

left = 0
right = max(A) + 10

while right - left > 1:
    mid = (left+right) // 2
    if f(mid):
        right = mid
    else:
        left = mid
print(right)