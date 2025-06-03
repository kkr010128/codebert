N = int(input())

MMM = map(int,input().split())
MM =list(MMM)
mini = 2020202020
list1 = []
total = 0
for i in MM:
  total+=i
  list1.append(total)
for i in list1:
  x = abs(total - 2*i)
  if mini > x:
    mini = x
print(mini)