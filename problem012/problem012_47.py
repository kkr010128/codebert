import math

num = raw_input()
num_list = []
for i in range(int(num)):
    a = raw_input()
    num_list.append(int(a))
count = 0

for num in num_list:
    if num <= 1:
        continue
    elif num == 2:
        count += 1
    elif num % 2 == 0:
        continue
    else:
        count += 1
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                count -= 1
                break
print count