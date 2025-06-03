three_num = input()
three_num = [int(i) for i in three_num.split(" ")]

a = three_num[0]
b = three_num[1]
c = three_num[2]

cnt = 0

for i in range(a, b + 1):
    if c % i == 0:
        cnt += 1

print(cnt)