five_numbers = list(map(int, input().split()))

for order, number in enumerate(five_numbers):
    if number == 0:
        if order == 0:
            print(five_numbers[order+1]-1)
            break
        print(five_numbers[order-1]+1)