X = int(input())
price = 100
year = 0
while price<X:
    price += price//100
    year += 1
print(year)