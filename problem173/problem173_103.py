N = int(input())
sum = 0
 
for i in range(1,N+1):
        if i % 3 == 0 and i % 5 == 0:
            i = ["FizzBuzz"]
        elif i % 3 == 0:
            i = ["Fizz"]
        elif i % 5 == 0:
            i = ["Buzz"]
    # if i % 3 == 0 and i % 5 == 0:
        else:
            sum += i
print(sum)