n = int(input())
lis = input().split()
dic = {}

for i in range(n):
  if lis[i] not in dic:
    dic[lis[i]] = 1
  else:
    dic[lis[i]] += 1
    
for x in dic.values():
  if x != 1:
    print("NO")
    exit()

print("YES")