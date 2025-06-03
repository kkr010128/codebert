x = int(input())
deposit = 100
year = 0
rate = 101
while(deposit < x):
  deposit = deposit * rate // 100
  year += 1
print(year)