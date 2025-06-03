nums = input().split(' ')
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])

multi = []
multi.append(a * c)
multi.append(a * d)
multi.append(b * c)
multi.append(b * d)

ans = - 10 ** 18
for i in range(4):
    if multi[i] > ans:
        ans = multi[i]

print(ans)