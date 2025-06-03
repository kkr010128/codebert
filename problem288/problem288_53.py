N = int(input())
x = int(N**(0.5)) + 1
while True:
    if N % x == 0:
        print((x-1)+((N//x)-1))
        break
    x -= 1
