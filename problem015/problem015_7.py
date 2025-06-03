def selection_sort(num_list):
    list_length = len(num_list)
    cnt = 0
    
    for i in range(list_length):
        min_element = i
        for j in range(i+1,list_length):
            if num_list[j] < num_list[min_element]:
                min_element = j
        if i != min_element:
            num_list[i],num_list[min_element] = num_list[min_element],num_list[i]
            cnt += 1
    return num_list,cnt

n = int(input())
num_list = list(map(int,input().split()))
ans_list,cnt = selection_sort(num_list)
str_ans_list = [str(i) for i in ans_list]
print('{}\n{}'.format(' '.join(str_ans_list),cnt))
