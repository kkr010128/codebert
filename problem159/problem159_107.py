X = int(input())
year = 0
deposit = 100
while deposit < X:
    deposit += int(str(deposit)[0: -2])
    year += 1
print(year)