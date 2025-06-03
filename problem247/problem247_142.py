from fractions import gcd
n, m = map(int, input().split())
a = [int(i)//2 for i in input().split()]


def lcm(x, y):
    return x*y//gcd(x, y)


l = 1
for i in a:
    l = lcm(l, i)
for i in a:
    if l//i % 2 == 0:
        print(0)
        exit()
print((m//l+1)//2)