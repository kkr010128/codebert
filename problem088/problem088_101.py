n = int(input())
a_list = list(map(int, input().split()))

dai = 0

for i in range(1, n):
    if a_list[i] < a_list[i-1]:
        dai += a_list[i-1] - a_list[i]
        a_list[i] += a_list[i-1] - a_list[i]
#        print(dai)
        
    else:
        continue

print(dai)