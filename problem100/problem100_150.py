n = int(input())

rate = 600
rank = 8

while True:
    if n < rate:
        print(rank)
        break
    rate += 200
    rank -= 1
