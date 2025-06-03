import math
 
i = input().split()
n = int(i[0])
D = int(i[1])
num_list = []
count = 0
for i in range(n):
	num_list.append(list(map(int,input().split())))
 
for j in num_list:
    x = j[0]
    y = j[1]
    dist = math.sqrt(x ** 2 + y ** 2)
    if dist <= D:
        count += 1
 
print(count)