N = int(input())
word = [str(input()) for i in range(N)]
dic = {}
for i in word:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
max_num = max(dic.values())
can_word = []
for i,j in dic.items():
  if j == max_num:
    can_word.append(i)
can_word.sort()
for i in can_word:
  print(i)