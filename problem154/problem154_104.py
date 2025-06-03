n, k = (int(x) for x in input().split())

# すぬけ君は全員お菓子を持っていないと仮定する
list_snuke = [str(i) for i in range(1, n + 1)]

# お菓子をもっているすぬけ君の番号を削除
# appendではなくリスト内包表記で書きたい
for i in range(0, k):
     d = int(input())
     a = [s for s in input().split()]
     for j in range(0, d):
         if a[j] in list_snuke:
             list_snuke.remove(a[j])

# お菓子をもっていないすぬけ君の人数を出力
print(len(list_snuke))