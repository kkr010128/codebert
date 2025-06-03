# input
N, M = map(int, list(input().split()))
A = list(map(int, input().split()))

# process
A.sort(reverse=True)

# 1回の握手の幸福度がx以上となるものの数、幸福度の合計を求める
def calc(x):
    count, sum = 0, 0

    j, t = 0, 0
    for i in reversed(range(N)):
        while j < N and A[i]+A[j] >= x:
            t += A[j]
            j += 1
        count += j
        sum += A[i]*j + t
    
    return (count, sum)

# 2分探索で答えを求める
def binary_search(x, y):
    mid = (x+y)//2

    count, sum = calc(mid)
    
    if count < M:
        return binary_search(x, mid)
    else:
        if x == mid:
            print(sum-(count-M)*mid)
        else:
            return binary_search(mid, y)

# 実行
binary_search(0, A[0]*2+1)
