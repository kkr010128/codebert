input()
num_list = raw_input().split()
num_list = map(int, num_list)

def selection_sort(num_list, count): 
    for i in range(0, len(num_list)):
        minj = i 
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[minj]:
                minj = j 
                temp = num_list[minj]
        if minj != i:
            num_list[minj] = num_list[i]
            num_list[i]= temp
            count += 1
        i += 1
    return count, num_list

count = 0 
count, num_list = selection_sort(num_list, count)
num_list = map(str, num_list)
print " ".join(num_list)
print count