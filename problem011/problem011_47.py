def gcd(a, b):
    c = max([a, b])
    d = min([a, b])
    if c % d == 0:
        return d
    else:
        return gcd(d, c % d)
        
nums = input().split()
print(gcd(int(nums[0]), int(nums[1])))
