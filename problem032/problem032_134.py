import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
p_1, p_2, p_3, p_infinit = 0, 0, 0, 0
dis_list = []
for i in range(n):
    dis_list.append(abs(x[i] - y[i]))
    sum_d = abs(x[i] - y[i])
    p_1 += sum_d
    p_2 += sum_d ** 2
    p_3 += sum_d ** 3
p_2 = math.sqrt(p_2)
p_3 = p_3 ** (1 / 3)

print(p_1)
print(p_2)
print(p_3)
print(max(dis_list))
