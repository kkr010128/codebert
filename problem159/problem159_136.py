X = int(input())
total = 100
count = 0
while total < X:
    total += total//100
    count += 1
print(count)
