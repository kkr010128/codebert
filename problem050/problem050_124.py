nums = []
while True:
    in_line = raw_input().split()
    h = int(in_line[0])
    w = int(in_line[1])
    if h == 0 and w == 0:
        break
    else:
        nums.append([h,w])
for num in nums:
    for i in range(0,num[0]):
        if i == 0 or i == num[0]-1:
            print "#"*num[1]
        else:
            print "#" + "."*(num[1]-2) + "#"
    print ""