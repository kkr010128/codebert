from collections import deque
n, k = input().rstrip().split(" ")
n = int(n)
k = int(k)
w_list = deque()
for _ in range(n):
    w_list.append(int(input().rstrip()))

def get_num_of_w(p, w_list, k):
    w_cnt = 0
    k_cnt = k
    temp_p = p
    temp_w_list = w_list.copy()

    while k_cnt > 0 and len(temp_w_list) > 0:
        w = temp_w_list[0]
        temp_p -= w
        if temp_p >= 0:
            temp_w_list.popleft()
            w_cnt += 1
        else:
            temp_p = p
            k_cnt -= 1
    return w_cnt  

    
left = 0
right = 10000 * 100000
min_p = 10000 * 100000
while left < right:
    mid = (left+right) // 2
    if get_num_of_w(mid, w_list, k) >= n:
        right = mid
        min_p = mid
    else:
        left = mid + 1
    
print(min_p)
    
    
    
    

        
    
    

        
    
