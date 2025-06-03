number_list=[int(i) for i in input().split()]
counter=0
for r in range(number_list[0],number_list[1]+1):
    if number_list[2]%r==0:
        counter+=1
print(counter)