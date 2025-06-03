N = int(input())
d_lst= [int(x) for x in input().split(' ')]
sum = 0
for i in range(len(d_lst)):
    for j in range(1+i,len(d_lst)):
        sum = sum + d_lst[i]*d_lst[j]
print(sum)