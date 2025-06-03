from collections import defaultdict
dic = defaultdict(int)
N = int(input())

for i in range(N):
  temp = str(input())
  dic[temp] += 1

MAX = max(dic.values())
ans = []
for x in dic.keys():
  if dic[x] == MAX:
    ans.append(x)
ans.sort()
print(*ans,sep="\n")