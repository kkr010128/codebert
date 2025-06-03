''' 1.降序排列，选出x个红苹果，y个绿苹果
    2.使用c个无色苹果去更新这x+y个苹果中的小值，直到最小也比无色苹果的大为止'''
nums = [int(i) for i in input().split()]
x = nums[0]
y = nums[1]
a = nums[2]
b = nums[3]
c = nums[4]
redApples = [int(i) for i in input().split()]
greenApples = [int(i) for i in input().split()]
colorless = [int(i) for i in input().split()]

redApples.sort(reverse=True)
greenApples.sort(reverse=True)
colorless.sort(reverse=True)
redApples = redApples[:x]
greenApples = greenApples[:y]

res = redApples+greenApples
res.sort(reverse=True)
currIndex = len(res)-1
for i in range(len(colorless)):
    if colorless[i] <= res[currIndex]:
        break
    res[currIndex] = colorless[i]
    currIndex -= 1
    if currIndex < 0:
        break

print(sum(res))
