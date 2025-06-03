n = int(input())
nums = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

li = []
for i in range(2**n):
    an = format(i, 'b').zfill(n)
    li.append(an)

ans = []
for lis in li:
    num = 0
    for i in range(n):
        if lis[i] == '1':
            num += nums[i]
    ans.append(num)

for j in m:
    if j in ans:
        print('yes')
    else:
        print('no')
