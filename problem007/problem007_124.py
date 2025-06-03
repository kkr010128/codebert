
fibo = [0] * 45
N = int(input())
fibo[0] = 1
fibo[1] = 1

for i in range(2,N+1):
    fibo[i] = fibo[i-1]+fibo[i-2]

print(fibo[N])
# N = int(input())　再帰のみ
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibo(n-1)+fibo(n-2)
# print(fibo(N))
# N = int(input()) メモ化再帰　5596KB 635B
# def fibo(n):
#     return fib2(1,1,n-1)
# def fib2(a,b,c):
#     if c < 1:
#         return a
#     return fib2(a+b,a,c-1)
# print(fibo(N))
