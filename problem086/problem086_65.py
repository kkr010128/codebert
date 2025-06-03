l = list(map(int, input().split()))
n = l[0]  # no of things he has to make
x = l[1]  # no of things he can make at a time
t = l[2]  # time taken for each set to be made = t
# 20 12 6 = 12
count = 0
while n > 0:
    n -= x
    count += t
print(count)
