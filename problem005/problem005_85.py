import sys
 
nums = []
 
 
for line in sys.stdin:
    nums.append(line)
 
for i in range(len(nums)):
    input_line = nums[i].split(" ")
    a = int(input_line[0])
    b = int(input_line[1])
 
    if a > b:
        num_bigger = a
        num_smaller = b
    else:
        num_bigger = b
        num_smaller = a

    r = 1   #?????????
    while r > 0:
        r = num_bigger % num_smaller
        num_bigger = num_smaller
        num_smaller = r

    max_common_div = num_bigger
    min_common_mpl = int((a * b)/max_common_div)
 
    print(str(max_common_div) + " " + str(min_common_mpl))