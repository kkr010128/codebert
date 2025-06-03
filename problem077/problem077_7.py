num = list(map(int,input().split()))

max_num = 0

max_num = num[0] * num[2]

max_num = max(max_num, num[0] * num[3])

max_num = max(max_num, num[1] * num[2])

max_num = max(max_num, num[1] * num[3])

print(max_num)