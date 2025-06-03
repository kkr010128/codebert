N = int(raw_input())
num_list = map(int, raw_input().split())

c = 0
flag = 1
while flag==1:
    flag =0
    for j in range(N-1,0,-1):
        if num_list[j] < num_list[j-1]:
            a = num_list[j]
            num_list[j] = num_list[j-1]
            num_list[j-1] = a
            c += 1
            flag =1

print " ".join(map(str,num_list))
print c