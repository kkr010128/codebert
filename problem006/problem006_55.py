n = int(raw_input())

debt=100000
for i in range(n):
  debt*=1.05
  if debt % 1000 != 0:
    debt = (int(debt / 1000)+1) * 1000
  else:
    debt = int(debt)
  
print debt