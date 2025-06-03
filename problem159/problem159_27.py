x = int(input())

sum = 100
year = 0

while x > sum:
    sum += sum//100
    year += 1

print(year)
