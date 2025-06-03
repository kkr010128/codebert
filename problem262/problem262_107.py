N = int(input())
tests = []
for n in range(N):
  A = int(input())
  tests_i = {}
  for a in range(A):
    x,y = map(int, input().split())
    tests_i[x-1] = y
  tests.append(tests_i)
# N人の人
# 正直者か真偽不明の発言者
# 人iがAi個の証言
# xijは正直物 if yij else 真偽不明の発言者

maximum = 0
import itertools
for Z in itertools.product(range(2), repeat=N):
  Z = list(Z)
#  print(Z)
  for i in range(N): # 人iの証言を検証
    honest = Z[i] # 正直ものか？
    for j,y in tests[i].items():
      if honest: #正直ものなら正しいはず
        if Z[j] != y:
#          print('NO')
          break
    else:
      # 証言が全て正しい
      continue
    break # 明らかに誤った証言をしたものがいる
  else:
#    print("ok")
    maximum = max(maximum, sum(Z))
print(maximum)