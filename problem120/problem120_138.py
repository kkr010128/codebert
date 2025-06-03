num = input().split(" ")
num_all = int(num[0])
count = int(num[1])
cost = list(map(int, input().split()))
cost.sort()
last = 0
for i in range(count):
  last += cost[i]
print(last)