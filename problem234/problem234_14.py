from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for n in range(1,N+1):
    s = str(n)
    dic[(int(s[0]), int(s[-1]))] += 1

res = 0
for key, value in dic.items():
    a, b = key
    cnt = dic.get((b,a),0)
    res += value * cnt

print(res)
