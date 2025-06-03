nums = []
while True:
    in_line = raw_input().split()
    if int(in_line[0]) == 0 and int(in_line[1]) == 0:
        break
    nums.append([int(in_line[0]),int(in_line[1])])
for n in nums:
    n.sort()
    print n[0],
    print n[1]