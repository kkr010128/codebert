debt=100000
week=input()

for i in range(week):
  debt=debt*1.05
  if debt%1000!=0:
    debt=int(debt/1000)*1000+1000

print debt