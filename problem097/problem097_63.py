K = int(input())

# 数列を漸化式と見て、順に余りを計算する
# 余りは循環するので、高々K項まで計算すれば、少なくとも1つの循環を抽出できるので十分
# あとは抽出した余りの列において、0が含まれるか、含まれる場合は何番目かを求める

i, a = 0, 0
l = []
for i in range(K):
  a = (10*a + 7) % K
  l.append(a)

j, ans = 0, -1
for j in range(K):
  if l[j] == 0:
    ans = j + 1
    break
    
print(ans)