payment = int(input())

count = 1
while True:
    if count * 1000 >= payment:
        print(count * 1000 - payment)
        break
    count += 1