import sys


n = int(input())

pmax = 10 ** 9 + 7

if n == 1 or n== 0 :
    print('0')
    sys.exit()
    
elif n == 2:
    print('2')
    sys.exit()


x = 10 ** n % pmax
y = 9 ** n % pmax
z = 9 ** n % pmax
yz = 8 ** n % pmax

ans = (x - y - z + yz) % pmax


print(ans)