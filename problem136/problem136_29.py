n = int(input())
#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table
a = prime_decomposition(n)
list_num=[]
for i,n in enumerate(a):
  if i ==0:
    list_num.append(n)
  if n in list_num:
    continue
  elif n not in list_num:
    list_num.append(n)
count = 0
for i in list_num:
  num = a.count(i)
  handan = True
  j = 1
  counter = 0
  while handan == True:
    num -=j
    if num<0:
      handan =False
    elif num>=0:
      counter+=1
      j+=1
  count +=counter

print(count)  