import numpy as np
n,m,k = list(map(int, input().split()))
a_list = np.array(input().split()).astype(int)
b_list = np.array(input().split()).astype(int)
a_sum =[0]
b_sum=[0]
for i in range(n):
    a_sum.append(a_sum[-1]+ a_list[i])
for i in range(m):
    b_sum.append(b_sum[-1] + b_list[i])
#print(a_sum, b_sum)
total = 0
num = m

for i in range(n+1):
    
    if a_sum[i] > k:
        break
    while (k - a_sum[i]) < b_sum[num]:
        num -=1
        #print(i, num)
        if num == -1:
            break
    total = max(i+num, total)
    
    
print(total)