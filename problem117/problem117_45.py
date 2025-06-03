import numpy as np
n,m,k = map(int,input().split())
a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))
a_csum = np.cumsum(a_ls)
b_csum = np.cumsum(b_ls)
def isOK(index, key, l):
    if l[index] > key:
        return True
    else:
        return False
def binary_search(l, key):
    '''
    keyより大きい値を持つ最小のインデックスを返す
    '''
    left = -1
    right = len(l)

    while (right - left) > 1:
        mid = left + (right - left) // 2
        # 直感的に記憶　
            # 「含まれている」んだったら「含むを許容（等号付き）する右側」はmidまで動かして問題ない
                # 新しいrightの位置がkeyの位置だとしても、「含む」は許容されてる
            # 「含まれていない」んだったら「含まない(<)左の壁」をそこまで動かしてもkeyを通り過ぎることはない
        if isOK(mid, key, l):
            right = mid
        else:
            left = mid
    
    # whileを抜ける時、rightとleftは一個差で、かつkeyがrightの位置にある
    return right
ans = 0
for i in range(n):
    rest = k - a_csum[i]
    if rest < 0:
        break
    ind = binary_search(b_csum, rest)
    canread_b = max(0,ind)
    canread = i+1 + canread_b
    ans = max(canread, ans)
rest = k
ind = binary_search(b_csum, rest)
canread_b = max(0,ind)
ans = max(canread_b, ans)

print(ans)



