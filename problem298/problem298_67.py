n, k = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0;
for i in l:
  if i >= k:
    cnt += 1;
print(cnt)