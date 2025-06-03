from collections import Counter
N = int(input())
aaa = list(map(int, input().split()))
acc = 0
cnt = Counter(aaa)
for v in cnt.values():
    acc +=  v * (v - 1) // 2
for i in range(N):
    print(acc - cnt[aaa[i]] + 1)
