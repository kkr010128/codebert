from fractions import gcd

n, m = [int(x) for x in input().split()]
a_list = [int(x) for x in input().split()]
a_h_list = [a // 2 for a in a_list]

count = set()
for a_h in a_h_list:
    temp = bin(a_h)
    count.add(len(temp) - temp.rfind("1"))

if len(count) == 1:
    temp = 1
    for a_h in a_h_list:
        temp *= a_h // gcd(a_h, temp)
    ans = (m // temp + 1) // 2
else:
    ans = 0

print(ans)