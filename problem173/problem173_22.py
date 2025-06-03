N = int(input())
sum = 0

if (1 <= N and N <= 10 ** 6):

    for i in range(1,N + 1):
        if ( i % 3 == 0) and ( i % 5 == 0):
        #if i % 15 ==0:
            N = 'Fizz Buzz'
        elif i % 3 == 0:
            N = 'Fizz'
        elif i % 5 == 0:
            N = 'Buzz'
        else:
            sum += i
    print(sum)
