n = int(input())
li = list(map(int, input().split()))
ans_li = [0] * n

for i in li:
  ans_li[i-1] += 1

for i in ans_li:
  print(i)