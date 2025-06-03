N = int(input())
A = list(map(int, input().split()))
x = 1
list1 = []

count = 0
for i in range(N):
  count += 1
  if A[i] == x:
    list1.append(i)
    count -= 1   
    x += 1
if list1 == []:
  print(-1)
else:
  print(count) 