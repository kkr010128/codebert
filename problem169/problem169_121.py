from collections import Counter
N = int(input())
As = list(map(int,input().split()))
cnt = Counter(As)
for i in range(1,N+1):
  print(cnt[i])