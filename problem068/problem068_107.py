str = input()
for q in range(int(input())):
    com, *num = input().strip().split()
    a, b = int(num[0]), int(num[1])
    if com == 'print':
        print(str[a:b+1])
    elif com == 'replace':
        str = str[:a] + num[2] + str[b+1:]
    else: # com == 'reverse'
        str = str[:a] + str[a:b+1][::-1] + str[b+1:]