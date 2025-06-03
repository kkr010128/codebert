def fibonacci(i, num_list):
    if i == 0 or i == 1:
        num_list[i] = 1
    else:
        num_list[i] = num_list[i-2] + num_list[i-1]

n = int(input()) + 1
num_list = [0 for i in range(n)]
for i in range(n):
    fibonacci(i, num_list)
print(num_list[-1])


