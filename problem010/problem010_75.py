num = raw_input()
num_list = raw_input()
num_list = num_list.split()
print " ".join(num_list)

 
for i in range(1, len(num_list)):
        num_list = map(int, num_list)
        temp = num_list[i]
        j = i - 1
        while (j >= 0 and num_list[j] > temp):
                num_list[j+1] = num_list[j]
                j -= 1
        num_list[j+1] = temp
        num_list = map(str, num_list)
        print " ".join(num_list)