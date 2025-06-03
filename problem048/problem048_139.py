n = input()
n = int(n)
x = raw_input()
x_list = x.split()
x_list = map(int, x_list)

max = x_list[0]
min = x_list[0]
sum = x_list[0]

for i in range(1, n):
    if max < x_list[i]:
        max = x_list[i]
    elif min > x_list[i]:
        min = x_list[i]
    sum += x_list[i]

print("%d %d %d" %(min, max, sum))