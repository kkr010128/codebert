from sys import exit
X = int(input())
x = 100
i = 0
while True:
    i += 1
    x *= 101
    x = x // 100

    if X <= x:
        print(i)
        exit()
