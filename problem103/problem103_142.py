n = int(input())
a_list = list(map(int, input().split()))

money = 1000
num = 0

for i in range(len(a_list)-1):
    if a_list[i] <= a_list[i+1]:
        num += money // a_list[i]
        money -= num * a_list[i]

        money += num * a_list[i+1]
        num = 0

print(money)
