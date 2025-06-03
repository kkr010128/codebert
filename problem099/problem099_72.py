N, K = map(int, input().split())
A = list(map(int, input().split()))
left = 0
right = max(A)
while(right - left > 1 and K != 0):
    x = (right + left) // 2
    def min_cut(x: int):
        n = 0
        for a in A:
            n += (a - 1) // x
        return n <= K
    if min_cut(x):
        right = x
    else:
        left = x
print(right)