tarop = hanakop = 0
for i in range(int(input())):
    taro, hanako = input().split()
    if taro > hanako:
        tarop += 3
    elif taro < hanako:
        hanakop += 3
    else:
        tarop += 1
        hanakop += 1
print(tarop, hanakop)