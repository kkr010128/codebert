def cardgame(animal1, animal2, taro, hanako):
    if animal1==animal2:
        return [taro+1, hanako+1]
    anim_list = sorted([animal1, animal2])
    if anim_list[0]==animal1:
        return [taro, hanako+3]
    else:
        return [taro+3, hanako]

n = int(input())
taro, hanako = 0, 0
for i in range(n):
    data = input().split()
    result = cardgame(data[0], data[1], taro, hanako)
    taro, hanako = result[0], result[1]
print(taro, end=" ")
print(hanako)

