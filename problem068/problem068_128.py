line = input()

num_query = int(input())

for loop in range(num_query):

    input_str = list(input().split())

    if input_str[0] == 'replace':
        left = int(input_str[1])
        right = int(input_str[2])
        right += 1
        line = line[:left] + input_str[3] + line[right:]

    elif input_str[0] == 'reverse':
        left = int(input_str[1])
        right = int(input_str[2])
        right += 1
        line = line[:left] + line[left:right][::-1] + line[right:]

    else: # print
        left = int(input_str[1])
        right = int(input_str[2])
        right += 1
        for i in range(left, right):
            print(line[i], end="")
        print()

