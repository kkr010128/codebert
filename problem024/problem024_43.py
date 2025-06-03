import math
n, k = map(int, input().split())
w = [int(input()) for i in range(n)]


def check(P): # 最駄積載量Pのk台のトラックで何個目の荷物まで積めるか。積める荷物の数をreturn
    i = 0
    for j in range(k):
        s = 0
        while (s + w[i]) <= P:
            s += w[i]
            i += 1
            if (i==n):
                return n
    return i

# 今、条件より1<=w<=10,000であり、1<=n<=100000
# つまり、トラックの最大積載量の取りうる最大値はこれらが一つのトラックに乗る時、つまり100000*10000
# 従ってこの範囲でPを探索すればよい
# 二分探索を使うことができる（これらのmidをPと仮定してcheckで積める個数を調べる
#→これがnよりも大きければPはもっと小さくて良いと言うことなのでrightをmidに、小さければleftをmidに！

        
def solve():
    left = 0
    right = 100000*10000
    while (right - left) > 1:
        mid = (left + right) / 2
        v = check(mid)
        if (v >= n):   # ?
            right = mid
        else:
            left = mid
            
    return right

ans = math.floor(solve())
print(ans)


