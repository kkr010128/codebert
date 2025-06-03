import copy
n,m = map(int,input().split())
a = set(list(map(int,input().split())))
a = list(a)
a_div2 = [0]*len(a)
a2 = copy.deepcopy(a)
# for i in range(len(a)):
#     if a[i] % 2 == 1:
#         print(0)
#         exit()
for i in range(len(a)):
    while a2[i] % 2 == 0:
        a2[i] //= 2
        a_div2[i] += 1
if len(set(a_div2)) != 1:
    print(0)
    exit()


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a,b):
    return a // gcd(a,b) * b


if len(a) == 1:
    if m < a[0]//2:
        print(0)
    else:
        print((m-a[0]//2)//a[0] + 1)
else:
    cnt = 1
    for i in range(len(a)):
        a[i] //= 2
        cnt = lcm(cnt,a[i])
    if m < cnt:
        print(0)
    else:
        print((m-cnt)//(cnt*2)+1)


