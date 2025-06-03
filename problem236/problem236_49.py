input_list = []
for i in range(0, 3):
  input_list.append(int(input()))

h = input_list[0]
w = input_list[1]
n = input_list[2]

temp_num = 0
if w <= h:
  temp_num = h
else:
  temp_num = w

answer = 0
if n % temp_num == 0:
  answer = int(n / temp_num)
else:
  answer = (n // temp_num) + 1
print(answer)