import sys
input = sys.stdin.readline
from bisect import bisect, bisect_left
from itertools import accumulate

def main():
    def check(x):
        count = 0
        for a in aaa:
            if x <= a:
                count += n
            else:
                count += n - bisect_left(aaa, x - a)
        return count >= m
    
    
    n, m = map(int, input().split())
    aaa = list(map(int, input().split()))
    aaa.sort()
    acc = [0] + list(accumulate(aaa))
    sum_a = acc[-1]
    
    l, r = 0, 200001
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    
    # 合計がlより大きい組み合わせの和と組数を求める→Mに足りない分だけ合計がlの組を採用
    ans = 0
    count = 0
    for a in aaa:
        if l <= a:
            ans += sum_a + a * n
            count += n
        else:
            omit = bisect(aaa, l - a)
            if omit < n:
                ans += sum_a - acc[omit] + a * (n - omit)
                count += n - omit
    ans += l * (m - count)
    print(ans)
    
if __name__ == '__main__':
    main()