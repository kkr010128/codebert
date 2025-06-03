#(40)フィボナッチ数列
n=int(input())
def fib(n):
    a=1
    b=1
    for _ in range(n):
        a,b=b,a+b
    return a
print(fib(n))
