import fractions

lst = []
for i in range(200):
    try:
        lst.append(input())
    except EOFError:
        break

nums = [list(map(int, elem.split(' '))) for elem in lst]

# gcd 
res_gcd = [fractions.gcd(num[0], num[1]) for num in nums]

# lcm
res_lcm = [nums[i][0] * nums[i][1] // res_gcd[i] for i in range(len(nums))]

for (a, b) in zip(res_gcd, res_lcm):
    print('{} {}'.format(a, b))