n = int(input())
a = list(map(int, input().split()))
sub_list = [0] * n

for i in (a):
  sub_list[i - 1] += 1

for i in range(n):
  print(sub_list[i], sep = ',')
