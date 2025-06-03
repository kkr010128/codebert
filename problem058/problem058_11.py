def find_ways(n, x):
    number_list = [i+1 for i in range(n)]
    cnt = 0
    for j in number_list:
        if j > n-2:
            break
        for k in number_list:
            if k <= j:
                continue
            l = x - j - k
            if l > n or l <= k:
                continue
            else:
                cnt += 1
    return cnt
 
while True:
    data = list(map(int, list(input().split())))
    if data[0] == 0 and data[1] == 0:
        break
    else:
        comb = find_ways(data[0], data[1])
        print(comb)

