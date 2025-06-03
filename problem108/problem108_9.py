n = int(input())
for i in range(11):
  ans = i*1000
  judge = ans-n
  if judge>=0:
    break
print(judge)
