def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

#bisect.bisect_left(list,key)はlistのなかでkey未満の数字がいくつあるかを返す
#つまりlist[i] < x となる i の個数
#bisect.bisect_right(list, key)はlistのなかでkey以下の数字がいくつあるかを返す
#つまりlist[i] <= x となる i の個数
#これを応用することで
#len(list) - bisect.bisect_left(list,key)はlistのなかでkey以上の数字がいくつあるかを返す
#len(list) - bisect.bisect_right(list,key)はlistのなかでkeyより大きい数字がいくつあるかを返す
#これらを使うときはあらかじめlistをソートしておくこと！
x,n = MI()
if n == 0:
  print(x)
else:
  p = set(LI())
  li = set(range(-1,102))
  new_li = li - p
  x_dis = []
  for k in new_li:
    x_dis.append(abs(k-x))
  ind = x_dis.index(min(x_dis))
  print(list(new_li)[ind])