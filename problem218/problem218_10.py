n=int(input())
s=[str(input()) for _ in range(n)]

from collections import Counter
results = Counter(s)

max_num = results.most_common()[0][1]
max_key_list = [kv[0] for kv in results.items() if kv[1] == max_num]
for i in sorted(max_key_list):
  print(i)
