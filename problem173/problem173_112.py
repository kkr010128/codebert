N = int(input())

amount = 0

for i in range(1, N + 1):
    is_fizzbuzz = (i % 3 == 0) or (i % 5 == 0)

    if not is_fizzbuzz:
        amount += i

print(amount)
