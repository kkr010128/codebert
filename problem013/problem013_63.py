dif_max = 1-10**9
min = 10**9
n_max = 0
n_max = int(raw_input())
 
price = [0]*n_max
for i in range(0, n_max):
  price[i] = int(raw_input())
for i in range(0, n_max-1):
  if min >= price[i]:
      min = price[i]
  if dif_max <= price[i+1] - min:
      dif_max = price[i+1] - min
print dif_max