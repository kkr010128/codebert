list_len = int(input().rstrip())
num_list = list(map(int, input().rstrip().split()))

for i in range(list_len):
    v = num_list[i]

    j = i - 1
    while j >= 0 and num_list[j] > v:
        num_list[j + 1] = num_list[j]
        j -= 1
    num_list[j+1] = v
    
    output_str = ' '.join(map(str, num_list))
    print(output_str)