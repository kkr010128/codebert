X = int(input())
deposit = 100
c = 0
while deposit < X:
    deposit = deposit + deposit//100
    c += 1
print(c)
