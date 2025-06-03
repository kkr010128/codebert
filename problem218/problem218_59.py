N = int(input())
S = [input() for _ in range(N)]

# ABC-081-Cの類題！
# 方針：各文字列の出現回数を数え、出現回数が最大なる文字列を昇順に出力する
 
# 各単語の出現回数を数える（辞書型を用いる！！）
dic = {}
for i in range(N):
  s = S[i]
  if s not in dic: dic[s] = 1
  else: dic[s] += 1

max_count = max(dic.values()) # 最大の出現回数
 
# 出現回数が最も多い単語を集計する
l = [key for key in dic.keys() if dic[key] == max_count]
 
# 昇順にソートして出力
for i in sorted(l):
  print(i)