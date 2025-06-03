n, k = map(int,input().split())

cnt = [0]*n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
      cnt[j-1] += 1
print(cnt.count(0))