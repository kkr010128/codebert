# 726 diff 1000
# 解法 836 XYへ到達する場合はどの経路も合計の長さは同じ = 動き方1,2の合計は同じ．
# なので合計値 L がわかればLについてmove1=i,move2=L-iとして，実際の経路の構成の仕方は,L_C_iなので

move1 = [1,2]
move2 = [2,1]
X,Y = map(int,input().split())
# まず，目的地へ到達できるか？到達できる場合は合計どれだけの移動量が必要かを計算する
max_move1 = int(Y/2)
move2_num = -1
move1_num = -1
for i in range(max_move1+1):
    rest = [X-i,Y-2*i]
    if (X-i) == 2*(Y-2*i):
        move1_num = i
        move2_num = (Y-2*i)
if move1_num == -1:
    print(0)
    exit()

# 到達するのに必要な合計の移動量がわかったので，それらの並べ替えについて考える．
# 求めるのは nCk　すなわち，いつもの奴
large = 10**9 + 7
# mod(x^p-1,p) = 1 よってmod(x^p-2,p) = 1/x となる.
ans = 1
for i in range(move1_num):
    ans *= (move1_num+move2_num - i)
    ans %= large
for j in range(2,move1_num+1):
    ans *= pow(j,large-2,large)
    ans %= large
print(ans)
