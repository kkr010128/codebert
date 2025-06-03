#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

x = int(input())

yokin = 100

for i in range(1, 100000000000):
    yokin *= 101
    yokin = yokin //100
    if (yokin >= x):
        print(i)
        break
