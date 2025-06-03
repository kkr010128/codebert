N = int(input())
list1 = []
for i in range(N+1):
  if i%3 ==0 or i%5 ==0:
    list1.append(i)

total1 =0
total2 = 0
for i in list1:
  total1 += i
for i in range(N+1):
  total2 += i
print(total2 -total1)