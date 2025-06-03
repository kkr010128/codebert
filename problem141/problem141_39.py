# C - Folia
import sys
readline = sys.stdin.readline

N = int(readline())
A = list(int(x) for x in readline().split())

# 上から順に取りうる頂点数を数えていく

leaf = sum(A) # 葉の残り数
tmp = 1 # 葉を除く頂点数
ans = 0 
for a in A:
    # その深さの葉の数が頂点数より多ければNG
    if tmp < a:
        ans = -1
        break
    # その深さまでで見た時、残りの葉の数と頂点数は一致（葉の数に合わせる）
    ans += min(tmp, leaf) 
    # その深さで使った葉の数を、葉の残り数と葉を除く頂点数からそれぞれ引いておく
    leaf -= a 
    tmp -= a 
    # 次の階層の頂点数の最大数は、葉を除く頂点数*2である
    tmp *= 2

print(ans)