N = int(input())
a = []
for i in range(N):
  a.append(input())
a = sorted(a)
count = 0
count_list=[]
b = []
for i,k in enumerate(a):
  if i == 0:
    continue
  if k == a[i-1]:
    count+=1
  else:
    count_list.append(count)
    b.append(a[i-1])
    count = 0
  if i==N-1:
    count_list.append(count)
    b.append(a[i])
maxi = 0
maxi_list =[]
for i,k in enumerate(count_list):
  if maxi <k:
    maxi_list.clear()
    maxi_list.append(b[i])
    maxi = k
  elif maxi == k:
    maxi_list.append(b[i])
  else:
    continue
for i in maxi_list:
  print(i)
    
         
