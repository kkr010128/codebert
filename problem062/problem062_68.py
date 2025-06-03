num_list=[]
while True:
    num = input()
    if num == 0:
        break
    num_list.append(num)

for num in num_list:
    print sum(map(int,list(str(num))))