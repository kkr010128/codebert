from math import sqrt

A, B = map(int, input().split())

def divisor(a, b):
    max_num = int(sqrt(a))
    divisor_list = []
    for i in range(1, max_num + 1):
        if a % i == 0 and b % i == 0:
            divisor_list.append(i)
            # for j in divisor_list:
            #     if a % (i*j) == 0 and b % (i*j) == 0:
            #         divisor_list.append(i)
            # divisor_list.append(i)
        tmp = a//i
        if a % tmp == 0 and b % tmp == 0:
            divisor_list.append(tmp)
            # for j in divisor_list:
            #     if a % (tmp*j) == 0 and b % (tmp*j) == 0:

    return list(set(divisor_list))

common_list = divisor(A, B)
common_list.sort()

# print(common_list)

length = len(common_list)
max_common = common_list[-1]
prods = []
dic = {c: 0 for c in common_list}

for i in range(1, length):
    for j in range(1, length):
        prod = common_list[i] * common_list[j]
        if prod > max_common:
            continue
        else:
            dic[prod] = 1
ans = 0
for c in common_list:
    if dic[c] == 0:
        ans += 1
        # print(c)

print(ans)