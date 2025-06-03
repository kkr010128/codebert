n = int(input())
from collections import defaultdict
dic = defaultdict(int)
for _ in range(n):
    tmp = input()
    dic[tmp] += 1
print(len(dic))