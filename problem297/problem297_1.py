#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

n = int(input())

if n == 1:
    print(1/1)
elif n % 2 == 0:
    print(1/2)
elif n % 2 != 0:
    print((n//2 + 1)/n)
