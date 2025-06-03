h = int(input())

counter = 0
while h > 0 :
    h //= 2
    counter += 1

print(pow(2, counter) - 1)