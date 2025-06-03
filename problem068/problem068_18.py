target = input()
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'print':
        print(target[int(order[1]):int(order[2])+1])
    elif order[0] == 'reverse':
        new_sent = ''
        begin_num=int(order[1])
        end_num=int(order[2])+1
        for i in range(len(target)):
            if begin_num <= i < end_num:
                new_sent += target[begin_num + end_num-1 -i]
            else:
                new_sent += target[i]
        target = new_sent
    else:
        target = target[:int(order[1])] + order[3] + target[int(order[2])+1:]

