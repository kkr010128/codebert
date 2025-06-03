
b=0
n=input()

for i in range(1, int(n)+1):

    if i%3==0 and i%5==0:
      a="FizzBuzz"
    elif i%3==0:
        a="Fizz"
    elif i%5==0:
      a="Buzz"
    else:
      b=b+i

print(b)




