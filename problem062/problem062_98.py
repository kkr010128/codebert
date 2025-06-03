sum_list=[]
while True:
    num=input()
    if num=='0':
        break
    num_list=list(num)
    for i in range(0,len(num_list)):
        num_list[i]=int(num_list[i])
    sum_list.append(sum(num_list))

for i in sum_list:
    print(i)