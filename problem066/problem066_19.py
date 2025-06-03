while True:
    str_shuffled = input()
    if str_shuffled == '-':
        break
    shuffle_time = int(input())
    for _ in range(shuffle_time):
        num_to_shuffle = int(input())
        str_shuffled = str_shuffled[num_to_shuffle:] + str_shuffled[:num_to_shuffle]
    print(str_shuffled)

