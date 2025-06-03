s = list(map(int, input().split()))
q = int(input())
# 上面をnとして時計回りにサイコロを回したときの正面のindexの一覧[a_1,a_2,a_3,a_4]
# 正面がa_nのとき右面はa_n+1
dm = {0: [1, 2, 4, 3, 1],
      1: [0, 3, 5, 2, 0],
      2: [0, 1, 5, 4, 0],
      3: [0, 4, 5, 1, 0],
      4: [0, 2, 5, 3, 0],
      5: [1, 3, 4, 2, 1]}

for i in range(q):
    t, f = map(lambda x: s.index(int(x)), input().split())
    print(s[dm[t][dm[t].index(f)+1]])

