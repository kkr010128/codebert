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
li = LI()
c = 1
i = 0
while c:
    if li[i] == 0:
        print(i+1)
        c = 0
    i += 1