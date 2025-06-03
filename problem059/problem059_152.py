list = [input().split()]
r = int(list[0][0])
c = int(list[0][1])
i = 0
k = 0
sum2 = 0
list3 = [0] * c
while i < r:
    sum = 0
    list2 = [input().split()]
    for j in list2[0]:
        print(j, end=' '),
        sum += int(j)
    for k in range(c):
        list3[k] += int(list2[0][k])
    print(sum)
    sum2 += sum
    i += 1
for l in list3:
    print(l, end=' ')
print(sum2)