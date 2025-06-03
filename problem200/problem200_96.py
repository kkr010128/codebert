import itertools 

line1 = input().split()
rei = input().split()
rei =list(map(int,rei))
den =input().split()
den =list(map(int,den))
cupon =[list(map(int,input().split())) for i in range(int(line1[2]))]

rei_mi = min(rei)
den_mi =min(den)

no_total =rei_mi +den_mi

for s in range(int(line1[2])):
  yes_total =int(rei[cupon[s][0]-1]) +int(den[cupon[s][1]-1]) - cupon[s][2]
  if no_total > yes_total:
    no_total =yes_total
print(no_total)
