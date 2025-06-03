from collections import Counter
 
N = int(input())
S = [input() for _ in range(N)]

# 方針：各文字列の出現回数を数え、出現回数が最大なる文字列を昇順に出力する
# Counter(リスト) は辞書型のサブクラスであり、キーに要素・値に出現回数という形式
# Counter(リスト).most_common() は(要素, 出現回数)というタプルを出現回数順に並べたリスト
S = Counter(S).most_common()

max_count = S[0][1] # 最大の出現回数

# 出現回数が最も多い単語を集計する
l = [s[0] for s in S if s[1] == max_count]

# 昇順にソートして出力
for i in sorted(l):
  print(i)