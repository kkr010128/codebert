# def f(n):
#     if n < 2:
#         return 1
#     else:
#         return n * f(n - 2)

# for i in range(2, 150, 2):
#     print(i, f(i))

N = int(input())

if N % 2 == 1:
    print(0)
    exit()

k = 10
cnt = 0
while k <= N:
    cnt += N // k
    k *= 5

print(cnt)
