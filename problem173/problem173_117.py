number = int(input())
Total = []

for i in range(1, number + 1):
    if number % 3 == 0 and i % 5 ==0:
        "FizzBuzz"
    elif i % 3 ==0:
        "Fizz"
    elif i % 5 == 0:
        "Buzz"
    else:
        Total.append(i)

print(sum(Total))
