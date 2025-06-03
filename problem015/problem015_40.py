N = int(raw_input())
num_list = map(int, raw_input().split())
c = 0

for i in range(0,N,1):
    flag =0
    minj =i
    for j in range(i,N,1):
        if num_list[j] < num_list[minj]:
            minj = j
            flag = 1
    c += flag
    num_list[i], num_list[minj] = num_list[minj], num_list[i]
print " ".join(map(str,num_list))
print c