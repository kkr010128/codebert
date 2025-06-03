import math

n = int(input())
folia = list(map(int, input().split()))
#print(n, folia)

#_1 木の一番下から順に各深さの頂点数[min, max]を取得
seq = [[folia[-1], folia[-1]]]
for i in range(n): # 深さ'n'分
    tmp = folia[-(i+2)]
    sml = math.ceil(seq[i][0] / 2) + tmp 
    big = seq[i][1] + tmp
    seq += [[sml, big]]
#print(seq)

#_2 一番根本の頂点数[min, max]に'1'を含まない場合は '存在しない木'
if not (seq[-1][0] <= 1 <= seq[-1][1]):
    print(-1)
    exit()

#_3 木の一番上から順に各深さで理論最大頂点数と'#_1のmax'との'min'をとる
ans =[1]
for j in range(n): # 深さ'n'分
    tmp = min((ans[j] - folia[j]) * 2, seq[-(j+2)][1])
    ans.append(tmp)
print(sum(ans)) # その合計が'ans'
