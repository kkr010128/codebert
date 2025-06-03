row_c, col_c = [int(x) for x in input().split(" ")]

nums =[]
col_sums = []
for i in range(row_c):
    nums.append([int(x) for x in input().split(" ")])

#calc each col
for i in range(col_c):
    s = 0
    for n in nums:
        s += n[i]
    col_sums.append(s)
col_sums.append(sum(col_sums))

#calc each row
for i, num in enumerate(nums):
    nums[i].append(sum(num))

#outpu
for row in nums:
    print(" ".join(map(str, row)))
print(" ".join(map(str, col_sums)))