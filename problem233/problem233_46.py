a = int(input())
b_list = list(map(int, input().split()))
count = 0
mini=a
for i in range(len(b_list)):
    if b_list[i] <= mini:
        count += 1
        mini = b_list[i]
        
print(count)