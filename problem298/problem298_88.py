num_persons, need_height = map(int, input().split())
a = map(int, input().split())
height_list = list(a)

count_height_ok = 0

for i in height_list:
    if i >= need_height:
        count_height_ok += 1

print(count_height_ok)
