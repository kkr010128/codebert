parent_list = []
while True:
    parent_list.append(input())
    if parent_list[-1] == '0':
        break

for n in parent_list[:-1]:
    sum = 0
    for c in n:
        sum += int(c)
    print(sum)