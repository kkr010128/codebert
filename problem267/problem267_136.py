n = int(input())
s = input()

# 3桁の番号を作るにあたり、文字列から抽出して作るのではなく、000〜999までの組み合わせが存在するかを確認する。
ans = 0
for i in range(10):
  a = s.find(str(i))
  for j in range(10):
    b = s.find(str(j), a+1) # aの取得位置の次から検索を行う
    for k in range(10):
      c = s.find(str(k), b+1) # bの取得位置の次から検索を行う
      if a == -1 or b == -1 or c == -1: continue
      else: ans += 1
print(ans)