num_list = list(map(int, input().split()))
num = num_list[0]
distance = num_list[1]
res = 0

for i in range(num):
    nmb_list = list(map(int, input().split()))
    if(nmb_list[0]*nmb_list[0]+nmb_list[1]*nmb_list[1] <= distance*distance):
        res += 1
        
print(res)