n = int(input())
dic = {}
for _ in range(n):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
mv = max(dic.values())
for s, v in sorted(dic.items()):
    if v == mv:
        print(s)