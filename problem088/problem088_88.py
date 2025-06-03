n = input()
list_height = list(map(int, input().split()))
pre = 0
max_chair = 0
list_chair = list()
for i in list_height:
    if i < pre:
        max_chair = pre - i
        pre = i + max_chair
        list_chair.append(max_chair)
    else:
        pre = i
print(sum(list_chair))