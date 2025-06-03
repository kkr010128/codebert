import sys
N = int(input())
cc = list(map(int,input().split()))
dic = set()
for i in cc:
  if i in dic:
    print('NO')
    sys.exit()
  else:
    dic.add(i)
print('YES')