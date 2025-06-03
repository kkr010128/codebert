num = raw_input()
num_list = []
for i in range(int(num)):
    a = raw_input()
    num_list.append(int(a))

min_ans = num_list[0]
max_ans = float("-inf")
for i in num_list[1:]:
    if i - min_ans > max_ans:
        max_ans = i - min_ans
    if i < min_ans:
        min_ans = i

print max_ans