N = int(input())
cc = map(int,input().split())
min_num = N
count = 0
for i in cc:
  if i <= min_num:
    min_num = i
    count += 1
print(count)