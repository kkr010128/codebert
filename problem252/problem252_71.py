from bisect import bisect_left

N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# 一回の握手でとりうる最大の得点+1
hi = 2*10**5+1
lo = 0


# 一回の握手で得られる幸福度がmid以上になるような握手のみで、握手回数がM回を超えるか調べていく
while hi - lo > 1:
    mid = (hi+lo)//2
    # 左手の得点をaとしたときに一回の握手でmid点以上得られる握手の組み合わせの数
    cnt_hs = 0
    for a in A:
        # 左手の得点がaのとき、midを超えるにはもう一方の右手でmid-x以上の点をとる必要がある
        right = mid - a
        idx = bisect_left(A, right)
        # Aのうち、idxより先のものを選べばその握手の点がmidを超える
        cnt_hs += N - idx
    
    # mid以上の点を得られる握手の組み合わせの数がMを超えているな、必要以上に握手しているから、握手回数を減らす方向に調整
    if cnt_hs >= M:
        lo = mid
    else:
        hi = mid
        

# M回以上の握手するには一回の握手で何点とりましょう、という点の最低ラインloが求まった

B = sorted(A, reverse=True)
accum_B = [0]*N
accum_B[0] = B[0]
for i in range(1,N):
    accum_B[i] = accum_B[i-1] + B[i]

ans = 0
cnt_hs = 0
for a in A:
    # 一回の握手でlo点以上得るためにとるべき、右手の最低点
    right = lo - a
    # aを使った場合はlo点以上とれないならスキップ
    if A[-1] < right:
        continue
    idx = bisect_left(A, right)
    # aをN-idx回と、Aについてidxより先の部分の和の合計を得る
    # sum(A[idx:])みたいにできなくもないけど毎回計算するより累積でやる方が効率いい
    ans += a*(N-idx) + accum_B[N-1 - idx]
    # lo点以上得られる握手回数を累計
    cnt_hs += N-idx

# 設定回数以上握手している場合はその分減らす
# 一回の握手の最低点がloなので、一回オーバーするごとにlo減らす？
# とりうる握手の最低点はloだけど、この設定において実際の握手の最低点はloになっていて、本当にそれが複数あるのか？
if cnt_hs > M:
    ans -= (cnt_hs - M) * lo

print(ans)