#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

n, a, b = map(int, input().split())


if (a == 0):
    print (0)
    exit()

ans = n // (a+b) * a

amari = n % (a+b)
if (amari <= a):
    ans += amari
else:
    ans +=a

print (ans)

