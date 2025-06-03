x = int(input())
c = 0
bank = 100
while bank < x:
  bank += bank//100
  c += 1
print(c)