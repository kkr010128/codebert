num_list = input().split()

i = 0
while True:
    if int(num_list[i]) == 0:
        print(i + 1)
        break
    i += 1