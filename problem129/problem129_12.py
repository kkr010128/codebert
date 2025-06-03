n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
m = arr[-1]
li = [0]*(m+1)
cnt = 0
        
for i in arr:
  for j in range(i, m+1, i):
    li[j] += 1

for i in arr:
  if li[i] == 1:
    cnt += 1

print(cnt)