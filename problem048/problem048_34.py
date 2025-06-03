sum = 0
n = input()
num = sorted(list(map(int, input().split())))
for i in range(int(n)):
    sum += num[i]
print("{} {} {}".format(num[0], num[-1], sum))
