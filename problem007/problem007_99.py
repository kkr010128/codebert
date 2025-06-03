n=int(input())
def func(n):
    fibonacci = [1,2]
    for i in range(2,n):
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    return fibonacci[n-1]
print(func(n))
