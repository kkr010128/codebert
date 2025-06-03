counts_number = int(input())
tmp_map = map(int, input().split())
num_list = list(tmp_map)
even_of_num_list = []
approve_counts = 0

for i in num_list:
    if i % 2 == 0:
        even_of_num_list.append(i)

for x in even_of_num_list:
    if x % 3 == 0 or x % 5 == 0:
        approve_counts += 1

if approve_counts == len(even_of_num_list):
    print('APPROVED')
else:
    print('DENIED')