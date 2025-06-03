N = int(input())
cc = list(map(int,input().split()))
num = [0]*N
for i in cc:
  num[i-1] += 1
for i in num:
  print(i)