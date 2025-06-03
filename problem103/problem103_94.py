n = int(input())
a_nums = list(map(int, input().split()))
money = 1000
stock = 0
for i in range(n):
    if i != n - 1 and a_nums[i] < a_nums[i + 1]:
        times = money // a_nums[i]
        stock += times
        money -= a_nums[i] * times
    elif i == n - 1 or a_nums[i] > a_nums[i + 1]:
        money += stock * a_nums[i]
        stock = 0
print(money)