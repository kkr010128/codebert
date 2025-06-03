num = raw_input()
num_list = raw_input().split()
num_list = map(int, num_list)
count = 0 

def bubble_sort(num_list, count):
    flag = True
    i = 0 
    while flag:
        flag = False
        for j in range(len(num_list)-1, i, -1):
            if num_list[j-1] > num_list[j]:
                temp = num_list[j]
                num_list[j] = num_list[j-1]
                num_list[j-1] = temp
                count += 1
                flag = True
        i += 1
    return count

count = bubble_sort(num_list, count)

num_list =  map(str, num_list)
print " ".join(num_list)
print count